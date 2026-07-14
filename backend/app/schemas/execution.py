from datetime import datetime

from pydantic import BaseModel


class ExecutionBase(BaseModel):
    pipeline_id: int
    status: str
    created_at: datetime


class ExecutionCreate(ExecutionBase):
    pass


class Execution(ExecutionBase):
    id: int

    class Config:
        from_attributes = True
