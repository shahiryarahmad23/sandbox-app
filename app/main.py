from fastapi import FastAPI,HTTPException,Depends
from app.models.note import Note
from app.db import Base,engine,get_db
from app.schema import NoteCreate,NoteRead
from sqlalchemy.orm import Session
from sqlalchemy import select


app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.get("/health")
def health():
    return {"Status":"ok"}

@app.post("/notes",response_model=NoteRead,status_code=201)
def create_note( note : NoteCreate , db : Session = Depends(get_db)):
        new_note = Note(
            body = note.body
        )
        db.add(new_note)
        db.commit()
        db.refresh(new_note)
        return new_note
    
    
@app.get("/notes",response_model=list[NoteRead],status_code=200)
def get_notes(db : Session = Depends(get_db)):
    stmt = select(Note)
    reuslt = db.execute(stmt).scalars().all()
    return reuslt


@app.get("/notes/{note_id}",response_model=NoteRead,status_code=200)
def get_id(note_id : int , db : Session = Depends(get_db)):
    
    stmt = select(Note).where(Note.id == note_id)
    result = db.execute(stmt).scalar_one_or_none()
    if result is None:
        raise HTTPException(status_code=404, detail="Id not found")
    return result
    



    
    
    
    

