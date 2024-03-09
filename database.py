from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from table import table

engine = create_engine('sqlite:///db/1.db', echo=False)
Base = declarative_base()

User = table.User
Queue = table.Queue
Projects = table.Projects
Base = table.Base


Base.metadata.create_all(engine)

Session = sessionmaker(
    engine,
    expire_on_commit=False,
)
session = Session()

