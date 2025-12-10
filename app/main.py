from fastapi import FastAPI
# import redis.asyncio as redis
import os
from fastapi.staticfiles import StaticFiles
from starlette.requests import Request
from fastapi.templating import Jinja2Templates
from starlette.responses import HTMLResponse, RedirectResponse
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from routes.ai_router import router as ai_router
from routes.gu import router as gu_router
from routes.category import router as category_router
from routes.result import router as result_router


app = FastAPI()

# -----------------------
# CORS 설정
# -----------------------
origins = [
    "http://localhost:5173",   # 프론트엔드 도메인 예시
    "http://localhost:8000",
    "http://127.0.0.1:8000",
    "http://127.0.0.1:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,           # 허용할 도메인
    allow_credentials=True,          # 쿠키, 인증 정보 허용
    allow_methods=["*"],             # 모든 HTTP 메서드 허용
    allow_headers=["*"],             # 모든 헤더 허용
)


# 정적 파일 제공 (CSS/JS/이미지)
app.mount("/static", StaticFiles(directory="static"), name="static")
app.mount("/assets", StaticFiles(directory="static/assets"), name="assets")
app.mount("/src", StaticFiles(directory="static/src"), name="src")

app.include_router(ai_router, prefix="/ai", tags=["AI"])
app.include_router(gu_router, prefix="/gu", tags=["GU"])
app.include_router(category_router, prefix="/category", tags=["Category"])
app.include_router(result_router, prefix="/result", tags=["Result"])


templates = Jinja2Templates(directory="templates")
@app.get("/")
def root(request: Request):
    return templates.TemplateResponse("index4.html", {"request": request})

@app.get("/.well-known/appspecific/com.chrome.devtools.json")
async def chrome_devtools_config():
    return JSONResponse(
        content={
            "Browser": "FastAPI-DevTools/1.0",
            "Protocol-Version": "1.3",
            "User-Agent": "FastAPI Server",
            "V8-Version": "0.0",
            "WebKit-Version": "0.0",
            "webSocketDebuggerUrl": "ws://127.0.0.1:8001/devtools",
            "targets": [
                {
                    "description": "FastAPI Debug Target",
                    "devtoolsFrontendUrl": "chrome-devtools://devtools/bundled/inspector.html",
                    "id": "fastapi-debug-1",
                    "title": "FastAPI App",
                    "type": "page",
                    "url": "http://localhost:8001",
                    "webSocketDebuggerUrl": "ws://127.0.0.1:8001/devtools/page/fastapi-debug-1"
                }
            ]
        }
    )

