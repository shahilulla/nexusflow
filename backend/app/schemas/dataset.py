from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class DatasetBase(BaseModel):
    name: str
    description: str | None = None
    source_type: str
    storage_type: str
    file_format: str
    owner: str
    schema_version: str = "1.0"
    status: str = "ACTIVE"


class DatasetCreate(DatasetBase):
    pass


class DatasetUpdate(BaseModel):
    name: str | None = None
    description: str | None = None
    source_type: str | None = None
    storage_type: str | None = None
    file_format: str | None = None
    owner: str | None = None
    schema_version: str | None = None
    status: str | None = None


class DatasetResponse(DatasetBase):
    id: UUID
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)