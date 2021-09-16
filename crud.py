from sqlalchemy.orm import Session

import models
import schemas

def get_user(db: Session, user_id:int):
    return db.query(models.User).filter(models.User.id == user_id).first()



def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()



def update_user(db: Session, user: schemas.User):
    db_user = models.User(**user.dict())
    cnt = db.query(models.User).filter(models.User.id == db_user.id).update({models.User.first_name : db_user.first_name,
                                                                        models.User.last_name:db_user.last_name,
                                                                        models.User.email: db_user.email,
                                                                        models.User.gender: db_user.gender,
                                                                        models.User.ip_address: db_user.ip_address,
                                                                        models.User.country_code: db_user.country_code },synchronize_session="fetch")
    db.commit()
    if cnt:
        return db.query(models.User).filter(models.User.id == db_user.id).first()



def del_user(db: Session, user_id:int):
    cnt = 0
    print(str(cnt))
    cnt =  db.query(models.User).filter(models.User.id == user_id).delete(synchronize_session=False)
    print(str(cnt))
    if cnt:
        res = "{} rows wih id: {} deleted successfully".format(cnt,user_id)
        db.commit()
    return res



def create_user(db: Session, user: schemas.User):
    db_user = models.User(**user.dict())
    # print("First name: " + db_user.first_name)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
    
