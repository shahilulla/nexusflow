from uuid import UUID

from sqlalchemy.orm import Session

from app.exceptions import (
    DatasetAlreadyExistsException,
    DatasetNotFoundException,
)
from app.repositories.dataset_repository import DatasetRepository
from app.schemas.dataset import DatasetCreate, DatasetUpdate
from app.schemas.pagination import PageResponse


class DatasetService:
    def __init__(self, db: Session):
        self.repository = DatasetRepository(db)

    def create_dataset(self, dataset: DatasetCreate):
        existing = self.repository.get_by_name(dataset.name)

        if existing:
            raise DatasetAlreadyExistsException(dataset.name)

        return self.repository.create(dataset)

    def get_datasets(
        self,
        page: int,
        size: int,
        search: str | None = None,
        status: str | None = None,
        owner: str | None = None,
        source_type: str | None = None,
        sort: str | None = None,
    ):
        items, total = self.repository.get_all(
            page=page,
            size=size,
            search=search,
            status=status,
            owner=owner,
            source_type=source_type,
            sort=sort,
        )

        return PageResponse.create(
            items=items,
            total=total,
            page=page,
            size=size,
        )

    def get_dataset(self, dataset_id: UUID):
        dataset = self.repository.get_by_id(dataset_id)

        if dataset is None:
            raise DatasetNotFoundException()

        return dataset

    def update_dataset(
        self,
        dataset_id: UUID,
        dataset: DatasetUpdate,
    ):
        db_dataset = self.repository.get_by_id(dataset_id)

        if db_dataset is None:
            raise DatasetNotFoundException()

        return self.repository.update(db_dataset, dataset)

    def delete_dataset(self, dataset_id: UUID):
        db_dataset = self.repository.get_by_id(dataset_id)

        if db_dataset is None:
            raise DatasetNotFoundException()

        self.repository.delete(db_dataset)

        return {
            "message": "Dataset deleted successfully"
        }