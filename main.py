from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

import models
from database import engine, get_db
import crud
import schemas

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello, FastAPI!"}


# 방명록 쓰기
@app.post("/new")
def new_note(new_note: schemas.Note, db: Session = Depends(get_db)):
    return {"id": crud.new_note(db, new_note)}


# 방명록 가져오기
@app.get("/notes")
def get_notes_all(db: Session = Depends(get_db)):
    return crud.get_notes_all(db)


# 방명록 모두 가져오기
@app.get("/notes/{id}")
def get_note(id: int, db: Session = Depends(get_db)):
    note = crud.get_note(db, id)

    if note is None:
        raise HTTPException(status_code=404, detail="Note not found")
    
    return note