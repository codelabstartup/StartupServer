from fastapi import APIRouter
from db.dbt_result import read_qs, read_ags
from db.dbt_ags import read_fp


router = APIRouter()

@router.get("/")
def result(gu: str, dong: str, category: str):
    body = {"gu": gu, "dong": dong, "category": category}
    qs_result = read_qs(body)
    ags_result = read_ags(body)
    fp_result = read_fp(body)
    return qs_result, ags_result, fp_result


