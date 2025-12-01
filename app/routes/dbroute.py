from fastapi import APIRouter
import os
import mysql.connector

router = APIRouter()

# MySQL 연결 함수
def get_mysql_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )
    
    
@router.get("/msyl")
def mysql_info():
    # MySQL 테스트
    conn = get_mysql_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT NOW();")
    result = cursor.fetchone()

    return {
        "mysql_time": result,
    }