from sqlalchemy.orm import Session

from app.repositories.pipeline_repository import PipelineRepository


class PipelineService:
    def __init__(self, db: Session):
        self.repository = PipelineRepository(db)

    def list_pipelines(self):
        return self.repository.list()
