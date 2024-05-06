from pydantic import BaseModel

# creating schemas for the User model
class UserBase(BaseModel):
    name: str
    pass

class UserCreate(UserBase):
    name: str
    id: int


class User(UserBase):
    id: int
    class Config:
        orm_mode = True