from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
DATABASE_URL = "mysql+mysqlconnector://webber:webber@localhost/test_unittest"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class orm_controller():
    def __init__(self):
        self.db = SessionLocal()
    def write_data(self,item):
        db_item = Item(name=item.name, description=item.description)
        self.db.add(db_item)
        self.db.commit()
        self.db.refresh(db_item)
        return db_item
    def read_data(self):
        items = self.db.query(Item).all()
        return items
    def read(self,tableToRead,dictToFilter={}):
        items = self.db.query(tableToRead).filter_by(**dictToFilter).all()
        return items
    def close(self):
        self.db.close()

class Item(Base):
    __tablename__ = "items"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
    description = Column(String(255))
    new_column = Column(String(255))
    
class Students(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
    description = Column(String(255))
    scource = Column(Integer)
    
    
Base.metadata.create_all(bind=engine)