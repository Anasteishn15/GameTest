from sqlalchemy import Column, Integer, String
from database import Base

class Players(Base):
   __tablename__ = "players"

   id = Column(Integer, primary_key=True)
   name = Column(String)
   hellos = Column(Integer, default=0)