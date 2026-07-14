from typing import List

from sqlalchemy.orm import Session

from app.models.pipeline import Pipeline


class PipelineRepository:
    def __init__(self, db: Session):
        self.db = db

    def list(self) -> List[Pipeline]:
        return self.db.query(Pipeline).all()
