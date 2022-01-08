from fastapi import APIRouter, Depends, FastAPI, HTTPException, status
from pydantic import BaseModel

router = APIRouter(
    prefix="/app",
    tags=["app"],
    responses={404: {"description": "Not found"}},
)

@router.get("/status")
async def server_status():
    try:
        return ({"status": "success", "data": True})
    except Exception as e:
        return({"status": "error", "data": str(e)})
