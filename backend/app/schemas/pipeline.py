from pydantic import BaseModel


class PipelineBase(BaseModel):
    name: str
    description: str | None = None


class PipelineCreate(PipelineBase):
    pass


class Pipeline(PipelineBase):
    id: int

    class Config:
        from_attributes = True
