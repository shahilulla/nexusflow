from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status

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
    dataset = service.get_dataset(dataset_id)

    if dataset is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Dataset not found",
        )

    return dataset


@router.put(
    "/{dataset_id}",
    response_model=DatasetResponse,
)
def update_dataset(
    dataset_id: UUID,
    dataset: DatasetUpdate,
    service: DatasetService = Depends(get_dataset_service),
):
    updated = service.update_dataset(dataset_id, dataset)

    if updated is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Dataset not found",
        )

    return updated


@router.delete(
    "/{dataset_id}",
    status_code=status.HTTP_200_OK,
)
def delete_dataset(
    dataset_id: UUID,
    service: DatasetService = Depends(get_dataset_service),
):
    deleted = service.delete_dataset(dataset_id)

    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Dataset not found",
        )

    return {
        "message": "Dataset deleted successfully"
    }