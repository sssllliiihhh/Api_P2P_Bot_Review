# -----------------------------------------------------------------------------
# Создание бд
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

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
class Projects(Base):
    __tablename__ = 'projects'

    id = Column(Integer, primary_key=True)
    text = Column(String(4096))
    link_to_git = Column(String(100))
    other_id = Column(Integer)
    qwe = relationship("Queue")


class Queue(Base):
    __tablename__ = 'queue'

    id = Column(Integer, primary_key=True)
#   номер ячейки ожидания
    user1 = Column(ForeignKey('projects.id'), primary_key=True)
    user2 = Column(ForeignKey('projects.id'), primary_key=True)


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
#
#
#     users = start_session()
#     text_to_return = session.query(Queue).filter(User.id == user_id).first()
#     return text_to_return
#
#
# # def create_text(user1: str, user2: str):
# #     new_text = Queue(text1=text1, other_id1=other_id1)
# #     session.add(new_text)
# #     session.commit()
