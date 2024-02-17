# -----------------------------------------------------------------------------
# Создание бд
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine('sqlite:///main.db', echo=False)
engine1 = create_engine('sqlite:///text.db', echo=False)

Base = declarative_base()
Base1 = declarative_base()


# -----------------------------------------------------------------------------
# main.db
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    other_id = Column(Integer)
    link_to_git = Column(String(100))


# text.db
class UserMessage(Base1):
    __tablename__ = 'message'

    id = Column(Integer, primary_key=True)
    text = Column(String(4096))
    link_to_git = Column(String(100))


# -----------------------------------------------------------------------------
# Инициализация бд

Base.metadata.create_all(engine)
Base1.metadata.create_all(engine1)

Session1 = sessionmaker(bind=engine1)
session1 = Session1()

Session = sessionmaker(bind=engine)
session = Session()


# -----------------------------------------------------------------------------
# Функции

def start_session(db):
    if db == "users":
        users = session.query(User).all()
        return users
    elif db == "users_message":
        users_message = session1.query(UserMessage).all()
        return users_message


def check(other_id):
    users = start_session("users")
    for user in users:
        if user.other_id == other_id:
            return False
    return True


def create_user(name=str, link_to_git=str, input_other_id=int):
    new_user = User(name=name, link_to_git=link_to_git, other_id=input_other_id)
    session.add(new_user)
    session.commit()


def return_user(user_id):
    users = start_session("users")
    i = 0
    for n in users:
        i += 1
    if i >= user_id:
        user_to_return = session.query(User).filter(User.id == user_id).first()
        return user_to_return
    else:
        return "Out of range"
