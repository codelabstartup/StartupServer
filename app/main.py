from fastapi import FastAPI
# import aiomysql
# import redis.asyncio as redis
import os
from fastapi.staticfiles import StaticFiles
from starlette.requests import Request
from fastapi.templating import Jinja2Templates
from starlette.responses import HTMLResponse, RedirectResponse
from db import bbs_db as db


app = FastAPI()

# @app.get("/")
# def root():
#     return "start page ok ..!!"
# 정적 파일 제공 (CSS/JS/이미지)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Redis
# redis_client = redis.from_url(os.getenv("REDIS_URL"))


templates = Jinja2Templates(directory="templates")
@app.get("/")
def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


# # MySQL 연결 테스트
# @app.get("/mysql")
# async def mysql_test():
#     conn = await aiomysql.connect(
#         host=os.getenv("MYSQL_HOST"),
#         user=os.getenv("MYSQL_USER"),
#         password=os.getenv("MYSQL_PASSWORD"),
#         db=os.getenv("MYSQL_DATABASE"),
#     )
#     async with conn.cursor() as cur:
#         await cur.execute("SELECT 1")
#         result = await cur.fetchone()
#     conn.close()
#     return {"mysql_result": result}


# # Redis 테스트
# @app.get("/redis")
# async def redis_test():
#     await redis_client.set("test_key", "Hello Redis")
#     value = await redis_client.get("test_key")
#     return {"redis_value": value.decode()}
