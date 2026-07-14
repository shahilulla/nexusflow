from fastapi import APIRouter

router = APIRouter(prefix="/pipelines", tags=["Pipelines"])

@router.get("")
def list_pipelines():
    return []
