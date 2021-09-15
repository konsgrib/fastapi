from typing import List, Optional

from pydantic import BaseModel


class UserBase(BaseModel):
    id: int


class UserCreate(UserBase):
    pass


class User(UserBase):
    id:int
    first_name:str
    last_name: Optional[str] = None
    email: Optional[str] = None
    gender: Optional[str] = None
    ip_address: Optional[str] = None
    country_code: Optional[str] = None

    class Config:
        orm_mode = True

