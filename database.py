from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 데이터베이스 URL
# 앱이 정상작동하도록 하려면 루트 디렉토리에 database.sqlite3 SQLite 파일이 있어야 합니다.
# sqlite3 database.sqlite3
DB_URL = "sqlite:///./database.sqlite3"

engine = create_engine(DB_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    
    try:
        yield db
    finally:
        db.close()