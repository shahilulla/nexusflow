from uuid import UUID

from sqlalchemy.orm import Session

from app.repositories.dataset_repository import DatasetRepository
from app.schemas.dataset import DatasetCreate, DatasetUpdate


class DatasetService:
    def __init__(self, db: Session):
        self.repository = DatasetRepository(db)

    def create_dataset(self, dataset: DatasetCreate):
        return self.repository.create(dataset)

    def get_datasets(self):
        return self.repository.get_all()

    def get_dataset(self, dataset_id: UUID):
        return self.repository.get_by_id(dataset_id)

    def update_dataset(
        self,
        dataset_id: UUID,
        dataset: DatasetUpdate,
    ):
        db_dataset = self.repository.get_by_id(dataset_id)

        if not db_dataset:
            return None

        return self.repository.update(db_dataset, dataset)

    def delete_dataset(self, dataset_id: UUID):
        db_dataset = self.repository.get_by_id(dataset_id)

        if not db_dataset:
            return False

        self.repository.delete(db_dataset)
        return True