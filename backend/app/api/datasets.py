from uuid import UUID

from fastapi import APIRouter, Depends, Query, status

from app.dependencies import get_dataset_service
from app.schemas.dataset import (
    DatasetCreate,
    DatasetResponse,
    DatasetUpdate,
)
from app.schemas.pagination import PageResponse
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
    response_model=PageResponse[DatasetResponse],
)
def get_all_datasets(
    page: int = Query(1, ge=1, description="Page number"),
    size: int = Query(10, ge=1, le=100, description="Items per page"),
    search: str | None = Query(
        None,
        description="Search by dataset name or description",
    ),
    status: str | None = Query(
        None,
        description="Filter by dataset status",
    ),
    owner: str | None = Query(
        None,
        description="Filter by dataset owner",
    ),
    source_type: str | None = Query(
        None,
        description="Filter by source type",
    ),
    sort: str | None = Query(
        None,
        description="Sort field (e.g. name, -created_at)",
    ),
    service: DatasetService = Depends(get_dataset_service),
):
    return service.get_datasets(
        page=page,
        size=size,
        search=search,
        status=status,
        owner=owner,
        source_type=source_type,
        sort=sort,
    )


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