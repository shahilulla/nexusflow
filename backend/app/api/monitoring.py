from fastapi import APIRouter

router = APIRouter(prefix="/monitoring", tags=["Monitoring"])

@router.get("")
def monitoring_status():
    return {"status": "ok"}
