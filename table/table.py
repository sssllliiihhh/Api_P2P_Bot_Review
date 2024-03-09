from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    other_id = Column(Integer)
    link_to_git = Column(String(100))


class Projects(Base):
    __tablename__ = 'projects'

    id = Column(Integer, primary_key=True)
    text = Column(String(4096))
    link_to_git = Column(String(100))
    other_id =  Column(Integer())#Column(ForeignKey("users.other_id"))
    user_id = Column(ForeignKey("users.id"))


class Queue(Base):
    __tablename__ = 'queue'

    id = Column(Integer, primary_key=True)
#   номер ячейки ожидания
    user1 = Column(ForeignKey('projects.id'), unique=True)
    user2 = Column(ForeignKey('projects.id'), unique=True)