from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from . import models, schemas, crud, database

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(title="Notes-API")


def get_db():
	db = database.SessionLocal()
	try:
		yield db
	finally:
		db.close()


@app.post("/notes/", response_model=schemas.NoteRead)
def create_note(note: schemas.NoteCreate, db: Session = Depends(get_db)):
	return crud.create_note(db, note)


@app.get("/notes/", response_model=list[schemas.NoteRead])
def read_notes(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
	return crud.get_notes(db, skip=skip, limit=limit)
