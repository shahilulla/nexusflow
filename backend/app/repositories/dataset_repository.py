from typing import List

from sqlalchemy.orm import Session

from app.models.dataset import Dataset


class DatasetRepository:
    def __init__(self, db: Session):
        self.db = db

    def list(self) -> List[Dataset]:
        return self.db.query(Dataset).all()
