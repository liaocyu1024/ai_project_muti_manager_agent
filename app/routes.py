from fastapi import APIRouter
from app.services.orchestrator import Orchestrator

router = APIRouter()
orch = Orchestrator()

@router.get("/report")
def generate_report():
    return orch.run_pipeline()
