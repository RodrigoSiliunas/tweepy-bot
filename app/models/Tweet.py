from sqlalchemy import Column, Integer, Float
from app.database import Base


class Tweet(Base):
    __tablename__ = 'tweets'

    id = Column(Integer, primary_key=True)
    dollar = Column(Float)
