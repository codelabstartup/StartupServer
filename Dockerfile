FROM python:3.12.10-slim

WORKDIR /app

# -----------------------------------------
# requirements 설치
# -----------------------------------------
COPY app/requirements.txt /app/requirements.txt
# ★ debugpy 추가
RUN apt-get update && apt-get install -y build-essential \
    && pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt \
    && pip install --no-cache-dir debugpy \        
    && apt-get remove -y build-essential && apt-get autoremove -y

# -----------------------------------------
# 애플리케이션 복사
# -----------------------------------------
COPY app /app

# -----------------------------------------
# debugpy로 uvicorn 실행 (디버깅 가능)
# -----------------------------------------
CMD ["python", "-m", "debugpy", "--listen", "0.0.0.0:5678", "--wait-for-client", "-m", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

