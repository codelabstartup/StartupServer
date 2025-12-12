from db.db_connection import get_connection

MYSQL_TABLE = "insight_post"

def insight_ps():
  try:
    con = get_connection()
    cursor = con.cursor()
    sql = f"""
        SELECT ip_id, ip_title, ip_content, ip_writer,
               ip_view_count, ip_created_at
        FROM {MYSQL_TABLE}
        ORDER BY ip_id DESC
    """
    cursor.execute(sql)
    rows = cursor.fetchall()
    columns = [col[0] for col in cursor.description]
    result_ps = [dict(zip(columns,row)) for row in rows]
    return result_ps
  except Exception as e:
    print("게시판 글 조회 오류:", e)
    return[]
  finally:
    if con:
      con.close()
      
def insight_ps_one(ip_id):
  try:
    con = get_connection()
    cursor = con.cursor()
    sql = f"""
        SELECT ip_id, ip_title, ip_content, ip_writer,
               ip_view_count, ip_created_at
        FROM {MYSQL_TABLE} WHERE ip_id = %s
    """
    cursor.execute(sql, (ip_id,))
    row = cursor.fetchone()
    columns = [col[0] for col in cursor.description]
    result_ps = dict(zip(columns,row))
    return result_ps
  except Exception as e:
    print("게시판 상세 페이지 오류:", e)
    return[]
  finally:
    if con:
      con.close()
      
def insight_ps_write(title, writer, content, password):
  try:
        con = get_connection()
        cursor = con.cursor()

        sql = f"""
            INSERT INTO {MYSQL_TABLE}
                (ip_title, ip_content, ip_writer, ip_pw)
            VALUES (%s, %s, %s, %s)
        """
        # 조회수는 처음 0으로, 나머지는 파라미터로 전달
        cursor.execute(sql, (title, content, writer, password))
        con.commit()

        # 방금 INSERT된 row의 PK (ip_id)
        return cursor.lastrowid

  except Exception as e:
        print("게시판 글 쓰기 오류:", e)
        return None

  finally:
        if con:
            con.close()
    
      


    
  