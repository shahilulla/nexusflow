from typing import List

from sqlalchemy.orm import Session

from app.models.execution import Execution


class ExecutionRepository:
    def __init__(self, db: Session):
        self.db = db

    def list(self) -> List[Execution]:
        return self.db.query(Execution).all()
