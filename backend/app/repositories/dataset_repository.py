from uuid import UUID

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

    def get_all(self):
        return self.db.query(Dataset).all()

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