import cx_Oracle

# Oracle Instant Client 초기화
try:
    cx_Oracle.init_oracle_client(lib_dir="C:\instantclient-basic-windows\instantclient_23_6")
    print("Oracle Instant Client 초기화 성공")
except cx_Oracle.DatabaseError as e:
    print("Oracle Instant Client 초기화 실패:", e)
    exit()

# SQLAlchemy를 이용한 DB 연결
from sqlalchemy import create_engine

engine = create_engine('oracle+cx_oracle://DB501_PROJ_G5:1234@203.249.87.57:1521/orcl')

try:
    with engine.connect() as connection:
        print("DB 연결 성공")
except Exception as e:
    print("DB 연결 실패:", e)