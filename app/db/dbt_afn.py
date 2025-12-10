from db.db_connection import get_connection
from pymysql import IntegrityError

MYSQL_TABLE = "ai_feature_name"

def read_featrue(body):
    try:
        con = get_connection()
        cursor = con.cursor()

        # 🔍 1) dong_code_master 에서 dcm_code 조회
        sql_dong = """
            SELECT dcm_code
            FROM dong_code_master
            WHERE dcm_gu = %s AND dcm_dong = %s
        """
        cursor.execute(sql_dong, (body["gu"], body["dong"]))
        dong_row = cursor.fetchone()
        if not dong_row:
            print("해당 지역의 dcm_code를 찾을 수 없습니다.")
            return []
        dcm_code = dong_row[0]

        # 🔍 2) svc_industry_code 에서 sic_code 조회
        sql_sic = """
            SELECT sic_code
            FROM svc_industry_code
            WHERE sic_industry_group = %s
        """
        cursor.execute(sql_sic, (body["category"],))
        sic_row = cursor.fetchone()
        if not sic_row:
            print("해당 업종의 sic_code를 찾을 수 없습니다.")
            return []
        sic_code = sic_row[0]

        # 🔍 3) ai_feature_name 에서 feature 값 조회
        sql = f"""
            SELECT 
                qs_log,
                qs_per_store,
                qs_total_diff_sqrt,
                store_density,
                comp_pres,
                comp_pres_pct,
                qs_per_store_pct,
                store_density_pct,
                qs_1114_pct,
                qs_1721_pct,
                qs_2124_pct,
                qs_weekdays_pct,
                qs_weekend_pct,
                qs_2030_pct,
                qs_3050_pct,
                qs_60_pct,
                fp_log,
                wp_log,
                rp_log,
                subway_station,
                bus_log,
                traffic_score,
                apt_cnt,
                apt_log
            FROM {MYSQL_TABLE}
            WHERE dong_cd = %s
              AND business_cd = %s
        """

        cursor.execute(sql, (dcm_code, sic_code))
        rows = cursor.fetchall()

        # 컬럼명 매핑
        columns = [col[0] for col in cursor.description]
        result = [dict(zip(columns, row)) for row in rows]
        return result

    except Exception as e:
        print("데이터 조회 오류:", e)
        return []

    finally:
        if con:
            con.close()