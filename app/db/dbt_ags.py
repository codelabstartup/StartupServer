from db.db_connection import get_connection
from pymysql import IntegrityError

MYSQL_TABLE = "float_populat"

def read_fp(body):
    try:
        con = get_connection()
        cursor = con.cursor()
        sql = "SELECT fp_total, yqc_code FROM float_populat WHERE dcm_code = (SELECT dcm_code FROM dong_code_master WHERE dcm_gu = %s AND dcm_dong = %s) order by yqc_code"
        cursor.execute(sql, (body["gu"], body["dong"]))
        rows = cursor.fetchall()
        columns = [col[0] for col in cursor.description]
        result_pop = [dict(zip(columns, row)) for row in rows]
        return result_pop
    except Exception as e:
        print(" 유동인구 조회 오류:", e)
        return []
    finally:
        if con:
            con.close()