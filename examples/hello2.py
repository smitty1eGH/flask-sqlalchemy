from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy                 import Column, Boolean, DateTime, Integer, String, ForeignKey, create_engine
from sqlalchemy.orm             import sessionmaker

Base = declarative_base()

class Todo( Base ):
    __tablename__ = 'todos'
    id            = Column('todo_id', Integer, primary_key=True)
    title         = Column(String(60))
    text          = Column(String)
    done          = Column(Boolean)
    pub_date      = Column(DateTime)

    def __init__(self, title, text):
        self.title = title
        self.text = text
        self.done = False

if __name__ == '__main__':
    engine  = create_engine( 'sqlite:///hello2.sqlite' )
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind = engine)
    sess    = Session()
    t0      = Todo("Hello", "World")
    sess.add(t0)
    sess.commit()
