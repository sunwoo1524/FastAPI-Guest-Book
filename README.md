# FastAPI와 SQLite로 만들어진 방명록 웹 서비스
## 실행 방법
아직 UI가 없습니다.   
API만 이용할 수 있습니다.   
루트 디렉토리에 database.sqlite3 SQLite3 데이터베이스 파일이 있어야 합니다.   
```
sqlite3 database.sqlite3
```

requirements.txt에 있는 파이썬 모듈들이 설치되어있어야 합니다.
```
pip install -r requirements.txt
```

uvicorn으로 웹 서버를 실행합니다.
```
uvicorn main:app
```

## API 문서 보기
```
http://localhost:8000/docs
```