from fastapi import APIRouter
from routes.dbt_member import read_one
import os

router = APIRouter()

@router.get("/")
def ai_root():
    result = read_one("apple")
    return {
        "ai": result,
    }