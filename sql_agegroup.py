from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from main.model import AgeGroup
from main import db
from sqlalchemy.orm import sessionmaker
# engine = create_engine('"postgresql://lony:lony@192.168.0.165:5432/postgres"', echo=True)
from sqlalchemy.ext.declarative import declarative_base

# Base = declarative_base()

from sqlalchemy.orm import sessionmaker



def create_ageGroup(session):
    print("inserting age records")

    session.add_all([
        AgeGroup(age_category='Pre School'),
        AgeGroup(age_category='KinderGarten'),
        AgeGroup(age_category='Elementary'),
        AgeGroup(age_category='Middle School'),
        AgeGroup(age_category='HighSchool'),
        AgeGroup(age_category='Pre UnderGrad')]
    )

if __name__ == '__main__':
    Session = sessionmaker(bind=db)
    session = Session()
    create_ageGroup(session)
    session.commit()
