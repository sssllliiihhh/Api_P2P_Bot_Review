from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker


engine = create_engine('sqlite:///main.db', echo=False)
Base = declarative_base()

engine1 = create_engine('sqlite:///text.db', echo=False)
Base1 = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    other_id = Column(Integer)
    link_to_git = Column(String(100))

class User(Base1):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    other_id = Column(Integer)
    link_to_git = Column(String(100))

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

users = session.query(User).all()

def check(other_id):
    for user in users:
        print(user.other_id, other_id)
        if user.other_id == other_id:
            return False
            break
    return True

def create_user(name=str, link_to_git=str, input_other_id=int):
    new_user = User(name=name, link_to_git=link_to_git, other_id=input_other_id)
    session.add(new_user)
    session.commit()


def return_user():
    for user in users:
        print(user.id, user.name, user.link_to_git, user.other_id)

