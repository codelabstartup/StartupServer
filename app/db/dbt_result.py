from db.db_connection import get_connection
from pymysql import IntegrityError


def read_qs(body):
    try:
        con = get_connection()
        cursor = con.cursor()
        sql = "SELECT qs_sales, qs_mon, qs_tue, qs_wed, qs_thu, qs_fri, qs_sat, qs_sun, yqc_code FROM quarter_sales WHERE dcm_code = (SELECT dcm_code FROM dong_code_master WHERE dcm_gu = %s AND dcm_dong = %s) AND sic_code = (SELECT sic_code FROM svc_industry_code WHERE sic_industry_group = %s) order by yqc_code"
        cursor.execute(sql, (body["gu"], body["dong"], body["category"]))
        rows = cursor.fetchall()
        columns = [col[0] for col in cursor.description]
        result_sales = [dict(zip(columns, row)) for row in rows]
        return result_sales
    except Exception as e:
        print("매출조회 오류:", e)
        return []
    finally:
        if con:
            con.close()
            
            
def read_ags(body):
    try:
        con = get_connection()
        cursor = con.cursor()
        sql = "SELECT ags_male, ags_female, yqc_code FROM age_gender_sales WHERE dcm_code = (SELECT dcm_code FROM dong_code_master WHERE dcm_gu = %s AND dcm_dong = %s) order by yqc_code"
        cursor.execute(sql, (body["gu"], body["dong"]))
        rows = cursor.fetchall()
        columns = [col[0] for col in cursor.description]
        result_pop = [dict(zip(columns, row)) for row in rows]
        return result_pop
    except Exception as e:
        print("유동인구 조회 오류:", e)
        return []
    finally:
        if con:
            con.close()