from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


from database import Base




class User(Base):

    __tablename__ = "users"


    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String, unique=True, index=True)
    gender = Column(String)
    ip_address = Column(String)
    country_code = Column(String)


