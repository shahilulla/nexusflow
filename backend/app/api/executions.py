from fastapi import APIRouter

router = APIRouter(prefix="/executions", tags=["Executions"])

@router.get("")
def list_executions():
    return []
