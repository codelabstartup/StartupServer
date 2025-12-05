from fastapi import APIRouter
from db.dbt_dcm import read_all
import os

router = APIRouter()

@router.get("/")
def ai_root():
    result = read_all()
    # result = "This is a placeholder response from the AI route."
    return {
        "ai": result,
    }