import cx_Oracle
from env import DATABASE
try:
    cx_Oracle.init_oracle_client(lib_dir="/opt/oracle/instantclient_23_3")
    print("Oracle Instant Client 초기화 성공")
except cx_Oracle.DatabaseError as e:
    print("Oracle Instant Client 초기화 실패:", e)
    exit()

# SQLAlchemy를 이용한 DB 연결
from sqlalchemy import create_engine

engine = create_engine(DATABASE.SQLALCHEMY_DATABASE_URI)

try:
    with engine.connect() as connection:
        print("DB 연결 성공")
except Exception as e:
    print("DB 연결 실패:", e)