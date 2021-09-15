from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import crud
import models
import schemas
from database import SessionLocal, engine
import uvicorn


models.Base.metadata.create_all(bind=engine)


app = FastAPI(debug=True)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# get user
@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user



# create new user
@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user(db,  user_id=user.id )
    if db_user:
        raise HTTPException(status_code=400, detail="User already registered")
    return crud.create_user(db=db, user=user)


@app.post("/new/", response_model=schemas.User)
def new_user(user:schemas.UserCreate,db:Session = Depends(get_db)):
    return crud.create_user(db=db, user=user)

# @app.get("/{id}")
# def get_user(id:int):
#     return {"id":id}





if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True,host='0.0.0.0',use_colors=True)
