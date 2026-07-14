from sqlalchemy.orm import Session

from app.repositories.dataset_repository import DatasetRepository


class DatasetService:
    def __init__(self, db: Session):
        self.repository = DatasetRepository(db)

    def list_datasets(self):
        return self.repository.list()
