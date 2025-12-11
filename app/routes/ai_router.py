from fastapi import APIRouter
from model import ai


router = APIRouter()

@router.get("/")
def ai_root(gu: str, dong: str, category: str):
    body = {"gu": gu, "dong": dong, "category": category}
    result = ai.predict_sales(body)
    print("AI Result:", result)
    return {
        "ai": result,
    }
    
    
if __name__ == '__main__':
    st = "ai.py"
    print(st)