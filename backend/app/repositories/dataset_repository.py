from uuid import UUID

from sqlalchemy import asc, desc, or_
from sqlalchemy.orm import Session

from app.models.dataset import Dataset
from app.schemas.dataset import DatasetCreate, DatasetUpdate


class DatasetRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, dataset: DatasetCreate):
        db_dataset = Dataset(**dataset.model_dump())

        self.db.add(db_dataset)
        self.db.commit()
        self.db.refresh(db_dataset)

        return db_dataset

    def get_all(
        self,
        page: int,
        size: int,
        search: str | None = None,
        status: str | None = None,
        owner: str | None = None,
        source_type: str | None = None,
        sort: str | None = None,
    ):
        query = self.db.query(Dataset)

        # Search
        if search:
            query = query.filter(
                or_(
                    Dataset.name.ilike(f"%{search}%"),
                    Dataset.description.ilike(f"%{search}%"),
                )
            )

        # Filters
        if status:
            query = query.filter(Dataset.status == status)

        if owner:
            query = query.filter(Dataset.owner == owner)

        if source_type:
            query = query.filter(Dataset.source_type == source_type)

        # Sorting
        if sort:
            descending = sort.startswith("-")
            field = sort[1:] if descending else sort

            if hasattr(Dataset, field):
                column = getattr(Dataset, field)
                query = query.order_by(
                    desc(column) if descending else asc(column)
                )
        else:
            query = query.order_by(desc(Dataset.created_at))

        total = query.count()

        items = (
            query
            .offset((page - 1) * size)
            .limit(size)
            .all()
        )

        return items, total

    def get_by_id(self, dataset_id: UUID):
        return (
            self.db.query(Dataset)
            .filter(Dataset.id == dataset_id)
            .first()
        )

    def get_by_name(self, name: str):
        return (
            self.db.query(Dataset)
            .filter(Dataset.name == name)
            .first()
        )

    def update(
        self,
        db_dataset: Dataset,
        dataset: DatasetUpdate,
    ):
        update_data = dataset.model_dump(exclude_unset=True)

        for key, value in update_data.items():
            setattr(db_dataset, key, value)

        self.db.commit()
        self.db.refresh(db_dataset)

        return db_dataset

    def delete(self, db_dataset: Dataset):
        self.db.delete(db_dataset)
        self.db.commit()