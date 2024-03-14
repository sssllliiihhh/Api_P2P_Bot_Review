from sqlalchemy import update
import database
from table import table


User = table.User
Queue = table.Queue
Projects = table.Projects
Variables = table.Variables


def check(other_id):
    session = database.Session()
    users = session.query(User).all()
    for user in users:
        if user.other_id == other_id:
            return False
    return True


def create_user(name: str, link_to_git=str, input_other_id=int):
    session = database.Session()
    new_user = User(name=name, link_to_git=link_to_git, other_id=input_other_id)
    session.add(new_user)
    session.commit()


def create_text(text: str, link_to_git: str, other_id: int):
    session = database.Session()
    message = Projects(text=text, link_to_git=link_to_git, other_id=other_id,
                       user_id=session.query(User).filter(User.other_id == other_id).first().id)
    session.add(message)
    session.commit()
    new_queue()


def return_user(user_id):
    session = database.Session()
    users = session.query(User).all()
    i = 0
    for n in users:
        i += 1
    if i >= user_id:
        user_to_return = session.query(User).filter(User.id == user_id).first()
        return user_to_return
    else:
        return "Out of range"


def check_link(link):
    if link.endswith('.git'):
        return True
    else:
        return False


def return_text(user_id):
    session = database.Session()
    users = session.query(User).all()
    text_to_return = session.query(Queue).filter(User.id == user_id).first()
    return text_to_return


def new_queue():
    session = database.Session()
    try:
        n = session.query(Variables).filter(Variables.i).first().i
        new_user = Queue(user1=n, user2=n+1)
        session.add(new_user)
        session.execute(
            update(Variables).
            where(Variables.i == n).
            values(i=n+2)
        )
        session.commit()
        return " Successfully added "
    except Exception as e:
        return e


def return_queue(id):
    session = database.Session()
    try:
        user1 = session.query(Projects).filter(Projects.id == Queue.user1).filter(Queue.id == id).first().text
        id1 = session.query(Projects).filter(Projects.id == Queue.user1).filter(Queue.id == id).first().other_id
        user2 = session.query(Projects).filter(Projects.id == Queue.user2).filter(Queue.id == id).first().text
        id2 = session.query(Projects).filter(Projects.id == Queue.user2).filter(Queue.id == id).first().other_id
    except:
        return " Out of range "
    if user1 and user2 is not None:
        return f" {user1} {id1} {user2} {id2}"
    else:
        if user1 is None and user2 is None:
            return " No review "
        else:
            return " Waiting for the last review "
