from fastapi import APIRouter
import os
import redis

router = APIRouter()

# Redis 연결
redis_client = redis.Redis(
    host=os.getenv("REDIS_HOST"),
    port=6379,
    decode_responses=True
)

@router.get("/info")
def user_info():
    # Redis 테스트
    redis_client.set("test_key", "hello redis")
    redis_value = redis_client.get("test_key")

    return {
        "redis_value": redis_value
    }