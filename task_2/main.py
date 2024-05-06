from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency to get database
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# post request to add user and return names of users with id greater than 5
@app.post("/adduser")
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user.id)
    if db_user:
        raise HTTPException(status_code=400, detail="User already registered")
    crud.create_user(db=db, user=user)
    names_with_ids_above_5 = crud.get_names_with_ids_above_5(db)
    return {"names_with_ids_above_5": names_with_ids_above_5}

# get request to return all users
@app.get("/users/", response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users

# get request to return user by id
@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user
