from typing import List, Optional

from pydantic import BaseModel


class User(BaseModel):
    id:int
    first_name:Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[str] = None
    gender: Optional[str] = None
    ip_address: Optional[str] = None
    country_code: Optional[str] = None

    class Config:
        orm_mode = True

