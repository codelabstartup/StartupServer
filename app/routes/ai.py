from fastapi import APIRouter
import os

router = APIRouter()

@router.get("/")
def ai_root():
    result = "AI Service is up and running!"
    return {
        "ai": result,
    }