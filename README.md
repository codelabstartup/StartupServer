이 문서는 FastAPI 서버를 MySQL, Redis와 함께 Docker로 실행하고  
Python 3.12.10 로컬 개발환경에서도 사용할 수 있도록 구성하는 방법을 안내합니다.

---

## 📌 1. 실행 방법

📌 윈도우 환경이면 Docker Desktop이 실행 되어있어야 한다.

### 🐳 Docker Compose 실행
```bash
docker-compose up --build
🚀 demon 실행
docker-compose up --build -d
docker-compose down
🚀 FastAPI 서버 접속

FastAPI:
👉 http://localhost:8000

Swagger UI:
👉 http://localhost:8000/docs

🗄️ MySQL 접속 정보

Host: localhost

Port: 3306

🔧 Redis 접속 정보

Host: localhost

Port: 6379

📌 2. 로컬(호스트) Python 3.12.10 가상환경

Docker 컨테이너 외에도 로컬 환경에서 직접 FastAPI 실행이 가능합니다.

🔧 Python 가상환경 생성
python -m venv venv

Windows
venv\Scripts\activate

패키지 설치
pip install -r app/requirements.txt

리눅스 실행
uvicorn main:app --host 0.0.0.0 --port 8001

윈도우 cmd 실행
start /min uvicorn main:app --host 0.0.0.0 --port 8001

📌 3. 구성 완료 (Features)

이 프로젝트에는 아래 요소가 포함됩니다:

✅ FastAPI 개발 서버 (Python 3.12.10)

✅ MySQL 8.0

✅ Redis 7.2

✅ Docker 기반 개발 환경

✅ .env 환경변수 관리

✅ DB 및 Redis 연결 테스트 API 포함

📌 4. env 파일 설정

✅ .env_backup 을 복사해서 .env파일로 만든다.

✅ mysql, redis 파일 경로를 PC 환경에 맞게 주정 : GIT_PATH=D:/_startupproject/StartupServer

✅ docker compose 로 docker 를 구성한다.




