from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker


engine = create_engine('sqlite:///example.db', echo=False)
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    age = Column(Integer)
    other_id = Column(Integer)


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

def create_user(name=str, age=int, input_other_id=int):
    new_user = User(name=name, age=age, other_id=input_other_id)
    session.add(new_user)
    session.commit()


def return_user():
    for user in users:
        print(user.id, user.name, user.age, user.other_id)

