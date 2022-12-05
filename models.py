from sqlalchemy import (create_engine, Column,
                                        String, Integer)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///pets.db', echo=True)
Session = sessionmaker()
session = Session()
Base = declarative_base(bind=engine)

class Pet(Base):
    __tablename__ = 'pets'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    pet_type = Column(String)

    def __repr__(self):
        return f'{self.id} | {self.name} {self.age} {self.pet_type}'


if __name__ == '__main__':
    Base.metadata.create_all(engine)