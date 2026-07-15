from fastapi import Depends
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.services.dataset_service import DatasetService


def get_dataset_service(
    db: Session = Depends(get_db),
) -> DatasetService:
    return DatasetService(db)