from sqlalchemy.orm import Session

from . import models, schemas


# return user by id
def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

# return all users
def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()

# create user
def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(name=user.name, id=user.id)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# return names of users with id greater than 5
def get_names_with_ids_above_5(db: Session):
    ans = []
    result = db.query(models.User.name).filter(models.User.id > 5).all()
    for name in result:
        ans.append(name[0])
    # return [name[0] for name in result]
    return ans
    
