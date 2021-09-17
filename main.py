from typing import List,Optional

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import crud
import models
import schemas
from database import SessionLocal, engine
import uvicorn
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
import jwt


models.Base.metadata.create_all(bind=engine)


app = FastAPI(debug=True)

JWT_SECRET = 'secret_seed'
# ==================================

oauth2_scheme= OAuth2PasswordBearer(tokenUrl='token')

@app.post('/token')
async def token(form_data: OAuth2PasswordRequestForm = Depends()):
    token = jwt.encode({'username':form_data.username}, JWT_SECRET)
    return {'access_token':token}
    # return {'access_token':form_data.username + '_token'}



# @app.get('/index')
# async def index(token: str = Depends(oauth2_scheme)):
#     return {'auth_token': token}
# ==================================

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# get user
@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db),token: str = Depends(oauth2_scheme)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


#get users
@app.get("/users/", response_model=List[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db),token: str = Depends(oauth2_scheme)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users



# create new user
@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.User, db: Session = Depends(get_db),token: str = Depends(oauth2_scheme)):
    db_user = crud.get_user(db,  user_id=user.id )
    if db_user:
        raise HTTPException(status_code=400, detail="User already registered")
    return crud.create_user(db=db, user=user)



#update or create user
@app.post("/users/{user_id}", response_model=schemas.User)
def update_user(user: schemas.User, db: Session = Depends(get_db),token: str = Depends(oauth2_scheme)):
    db_user = crud.get_user(db,  user_id=user.id )
    if db_user:
        return crud.update_user(db=db,user=user)
    else:
        return crud.create_user(db=db, user=user)



@app.delete("/users/{user_id}", response_model=str)
def del_user(user_id: int, db: Session = Depends(get_db),token: str = Depends(oauth2_scheme)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user:
        return crud.del_user(db=db,user_id=db_user.id)
    else:
        return "No records to delete with id: {}".format(user_id)



if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True,host='0.0.0.0',use_colors=True)