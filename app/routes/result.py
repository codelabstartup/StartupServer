from fastapi import APIRouter
from db.dbt_result import read_sales 
from db.dbt_result import read_age
from db.dbt_result import read_pop

router = APIRouter()

@router.get("/")
def result(gu: str, dong: str, category: str):
    body = {"gu": gu, "dong": dong, "category": category}
    sales_result = read_sales(body)
    age_result = read_age(body)
    pop_result = read_pop(body)
    return sales_result, age_result, pop_result


