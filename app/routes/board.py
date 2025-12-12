from fastapi import APIRouter, HTTPException, Request
from db.dbt_ip import insight_ps, insight_ps_write, insight_ps_one

router = APIRouter()

@router.get("/")
def select_bd():
  bd_list = insight_ps()
  print("게시판 리스트;", bd_list)
  return bd_list

@router.get("/{ip_id}")
def select_bd_one(ip_id:int):
  bd_one = insight_ps_one(ip_id)
  print("게시판 리스트;", bd_one)
  return bd_one


@router.post("/write")
async def write_bd_one(request: Request):
    """
    게시글 작성: 프론트에서 보내준 JSON 받아서 DB에 INSERT
    """
    data = await request.json()

    title = data.get("title")
    writer = data.get("writer")     # 프론트의 author -> DB ip_writer 로 매핑
    content = data.get("content")
    password = data.get("password")

    # 필수값 체크
    if not title or not writer or not content or not password:
        raise HTTPException(status_code=400, detail="필수 항목이 누락되었습니다.")

    new_id = insight_ps_write(title, writer, content, password)

    if not new_id:
        raise HTTPException(status_code=500, detail="게시글 저장에 실패했습니다.")

    return {"message": "등록 완료", "ip_id": new_id}

