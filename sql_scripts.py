from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from main.model import AgeGroup
from main import db
from main.model import Topics
from main.model import Subtopics
from main.model import Establishment
from main.model import TypeOfOrganization


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


def create_establishment(session):
    print("inserting places info")

    session.add_all([
        TypeOfOrganization(name='centralpark library', type='library', address='2635 Homestead Rd, Santa Clara, CA 95051',
                      placeLongitude=37.340541498562196, placeLatitude=-121.97339981532922),

        TypeOfOrganization(name='cupertino library', type='library', address='10800 Torre Ave, Cupertino, CA 95014',
                      placeLongitude=37.31802503178155, placeLatitude=-122.02871908649388),
        TypeOfOrganization(name='worlds in wild story time', type='virtual', address='https://www.wordsinthewild.org/storytime-with-words-in-the-wild'),
        TypeOfOrganization(name='Marines Mammal Monday', type='virtual', address='https://www.marinemammalcenter.org/education/adults-families/marine-mammal-monday'),
        TypeOfOrganization(name='cut Arts', type='online',
                      address='https://www.cutarts.com/'),
        TypeOfOrganization(name='chatBot space and Science Center', type='Science Center',
                      address='https://chabotspace.org/')


        ]
    )

def create_typeOfOrg(session):
    print("inserting places info")

    session.add_all([
        Establishment(name='centralpark library', type='library', address='2635 Homestead Rd, Santa Clara, CA 95051',
                      placeLongitude=37.340541498562196, placeLatitude=-121.97339981532922),

        Establishment(name='cupertino library', type='library', address='10800 Torre Ave, Cupertino, CA 95014',
                      placeLongitude=37.31802503178155, placeLatitude=-122.02871908649388),
        Establishment(name='worlds in wild story time', type='virtual', address='https://www.wordsinthewild.org/storytime-with-words-in-the-wild'),
        Establishment(name='Marines Mammal Monday', type='virtual', address='https://www.marinemammalcenter.org/education/adults-families/marine-mammal-monday'),
        Establishment(name='cut Arts', type='online',
                      address='https://www.cutarts.com/'),
        Establishment(name='chatBot space and Science Center', type='Science Center',
                      address='https://chabotspace.org/'),


        ]
    )

def create_topics(session):
    print("inserting topics ")

    session.add_all([
        Topics(topics_name='Family and parenting'),

        Topics(topics_name='Arts and Crafts for kids'),
        Topics(topics_name='cooking'),
        Topics(topics_name='Books'),
        Topics(topics_name='Tutor'),
        Topics(topics_name='outDoor Activities'),
        Topics(topics_name='playDate'),
        Topics(topics_name='Kids Volunteering'),
        Topics(topics_name='Online Resources'),
        Topics(topics_name='Games'),
        Topics(topics_name='Kids Health'),
        Topics(topics_name='Kids school Syllabus'),
        Topics(topics_name='DIY'),
        Topics(topics_name='After Care'),
        Topics(topics_name='Summer Camp'),
        Topics(topics_name='Activity')

        ]
    )


if __name__ == '__main__':
    Session = sessionmaker(bind=db)
    session = Session()
    # create_ageGroup(session)
    #create_establishment(session)
    create_topics(session)
    session.commit()
