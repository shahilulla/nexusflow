from sqlalchemy.orm import Session

from app.repositories.execution_repository import ExecutionRepository


class ExecutionService:
    def __init__(self, db: Session):
        self.repository = ExecutionRepository(db)

    def list_executions(self):
        return self.repository.list()
