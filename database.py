from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker


engine = create_engine('sqlite:///main.db', echo=True)
engine1 = create_engine('sqlite:///text.db', echo=True)

Base = declarative_base()
Base1 = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    other_id = Column(Integer)
    link_to_git = Column(String(100))


class UserMessage(Base1):
    __tablename__ = 'message'

    id = Column(Integer, primary_key=True)
    text = Column(String(4096))
    link_to_git = Column(String(100))


Base.metadata.create_all(engine)
Base1.metadata.create_all(engine1)

Session1 = sessionmaker(bind=engine1)
session1 = Session1()

Session = sessionmaker(bind=engine)
session = Session()

users = session.query(User).all()
users_message = session1.query(UserMessage).all()


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
