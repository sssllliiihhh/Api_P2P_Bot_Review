# -----------------------------------------------------------------------------
# Создание бд
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine('sqlite:///main.db', echo=False)

Base = declarative_base()


# -----------------------------------------------------------------------------
# main.db
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    other_id = Column(Integer)
    link_to_git = Column(String(100))


# text.db
class UserMessage(Base):
    __tablename__ = 'message'

    id = Column(Integer, primary_key=True)
    text = Column(String(4096))
    link_to_git = Column(String(100))
    other_id = Column(Integer)


class Queue(Base):
    __tablename__ = 'queue'

    id = Column(Integer, primary_key=True)
#   номер ячейки ожидания
    text1 = Column(String(4096))
    text2 = Column(String(4096))
    other_id1 = Column(Integer)
    other_id2 = Column(Integer)


# -----------------------------------------------------------------------------
# Инициализация бд
Base.metadata.create_all(engine)

# main.db
Session = sessionmaker(bind=engine)
session = Session()
# text.db


# -----------------------------------------------------------------------------
# Функции
# Запуск сессии для извлечения данных из базы
def start_session():
    users = session.query(User).all()
    return users


# Проверка есть ли строка с таким-же other_id в базе
def check(other_id):
    users = start_session()
    for user in users:
        if user.other_id == other_id:
            return False
    return True


# Запись данных в таблицу User
def create_user(name: str, link_to_git=str, input_other_id=int):
    new_user = User(name=name, link_to_git=link_to_git, other_id=input_other_id)
    session.add(new_user)
    session.commit()


# Возвращение строки из таблицы User
def return_user(user_id):
    users = start_session()
    i = 0
    for n in users:
        i += 1
    if i >= user_id:
        user_to_return = session.query(User).filter(User.id == user_id).first()
        return user_to_return
    else:
        return "Out of range"

# Проверка ссылки на гит
def check_link(link):
    if link.endswith('.git'):
        return True
    else:
        return "Not git link"
