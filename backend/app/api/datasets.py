from uuid import UUID

from fastapi import APIRouter, Depends, status

from app.dependencies import get_dataset_service
from app.schemas.dataset import (
    DatasetCreate,
    DatasetResponse,
    DatasetUpdate,
)
from app.services.dataset_service import DatasetService

router = APIRouter(
    prefix="/datasets",
    tags=["Datasets"],
)


@router.post(
    "",
    response_model=DatasetResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_dataset(
    dataset: DatasetCreate,
    service: DatasetService = Depends(get_dataset_service),
):
    return service.create_dataset(dataset)


@router.get(
    "",
    response_model=list[DatasetResponse],
)
def get_all_datasets(
    service: DatasetService = Depends(get_dataset_service),
):
    return service.get_datasets()


@router.get(
    "/{dataset_id}",
    response_model=DatasetResponse,
)
def get_dataset(
    dataset_id: UUID,
    service: DatasetService = Depends(get_dataset_service),
):
    return service.get_dataset(dataset_id)


@router.put(
    "/{dataset_id}",
    response_model=DatasetResponse,
)
def update_dataset(
    dataset_id: UUID,
    dataset: DatasetUpdate,
    service: DatasetService = Depends(get_dataset_service),
):
    return service.update_dataset(dataset_id, dataset)


@router.delete(
    "/{dataset_id}",
    status_code=status.HTTP_200_OK,
)
def delete_dataset(
    dataset_id: UUID,
    service: DatasetService = Depends(get_dataset_service),
):
    return service.delete_dataset(dataset_id)