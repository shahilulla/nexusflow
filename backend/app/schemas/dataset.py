from pydantic import BaseModel


class DatasetBase(BaseModel):
    name: str
    description: str | None = None


class DatasetCreate(DatasetBase):
    pass


class Dataset(DatasetBase):
    id: int

    class Config:
        from_attributes = True
