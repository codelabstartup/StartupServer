from fastapi import APIRouter
import os
# from catboost import CatBoostClassifier

router = APIRouter()

@router.get("/")
def ai_root():
    # result = read_one("apple")
    result = "This is a placeholder response from the AI route."
    return {
        "ai": result,
    }
    
    
if __name__ == '__main__':
    st = "ai.py"
    print(st)