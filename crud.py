from sqlalchemy.orm import Session

from models import GuestBook
from schemas import Note


# 방명록 쓰기
def new_note(db: Session, note: Note):
    note = GuestBook(
        name=note.name,
        date=note.date,
        note=note.note
    )
    db.add(note)
    db.commit()

    return note.id


# 방명록 가져오기
def get_note(db: Session, id: int):
    note = db.query(GuestBook).filter(GuestBook.id == id).first()
    return note


# 방명록 모두 가져오기
def get_notes_all(db: Session):
    notes = db.query(GuestBook).all()
    return notes