from typing import List, Optional

from pydantic import BaseModel


class UserBase(BaseModel):
    id: int


class UserCreate(UserBase):
    pass


class User(UserBase):
    id:int
    first_name:str
    last_name:str
    email:str
    gender:str
    ip_address:str
    country_code:str

    class Config:
        orm_mode = True