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
        TypeOfOrganization(name='centralpark library', type='library',
                           address='2635 Homestead Rd, Santa Clara, CA 95051',
                           placeLongitude=37.340541498562196, placeLatitude=-121.97339981532922),

        TypeOfOrganization(name='cupertino library', type='library', address='10800 Torre Ave, Cupertino, CA 95014',
                           placeLongitude=37.31802503178155, placeLatitude=-122.02871908649388),
        TypeOfOrganization(name='worlds in wild story time', type='virtual',
                           address='https://www.wordsinthewild.org/storytime-with-words-in-the-wild'),
        TypeOfOrganization(name='Marines Mammal Monday', type='virtual',
                           address='https://www.marinemammalcenter.org/education/adults-families/marine-mammal-monday'),
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
        Establishment(name='worlds in wild story time', type='virtual',
                      address='https://www.wordsinthewild.org/storytime-with-words-in-the-wild'),
        Establishment(name='Marines Mammal Monday', type='virtual',
                      address='https://www.marinemammalcenter.org/education/adults-families/marine-mammal-monday'),
        Establishment(name='cut Arts', type='online',
                      address='https://www.cutarts.com/'),
        Establishment(name='chatBot space and Science Center', type='Science Center',
                      address='https://chabotspace.org/'),

    ]
    )


def create_subtopics(session):
    print("inserting sub topics ")

    session.add_all([

        Subtopics(parent_topics_id=1,subtopics_name = 'parenting babies'),
        Subtopics(parent_topics_id=1, subtopics_name='parenting preschooler'),
        Subtopics(parent_topics_id=1, subtopics_name='parenting kindergartener'),
        Subtopics(parent_topics_id=1, subtopics_name='parenting middle-SchoolKids'),
        Subtopics(parent_topics_id=1, subtopics_name='parenting HighSchoolkids'),
        Subtopics(parent_topics_id=1, subtopics_name='oil painting'),
        Subtopics(parent_topics_id=2, subtopics_name='drawing'),
        Subtopics(parent_topics_id=2, subtopics_name='waterColoring'),
        Subtopics(parent_topics_id=2, subtopics_name='crafts with paper'),
        Subtopics(parent_topics_id=2, subtopics_name='crafts with reUsable materials'),
        Subtopics(parent_topics_id=2, subtopics_name='knitting'),
        Subtopics(parent_topics_id=2, subtopics_name='others'),
        Subtopics(parent_topics_id=3, subtopics_name='kids breakfast ideas'),
        Subtopics(parent_topics_id=3, subtopics_name='kids quick snacks ideas'),
        Subtopics(parent_topics_id=3, subtopics_name='lunch recipes'),
        Subtopics(parent_topics_id=3, subtopics_name='dinner recipes'),
        Subtopics(parent_topics_id=3, subtopics_name=' baking recipes'),
        Subtopics(parent_topics_id=3, subtopics_name='chicken recipes'),
        Subtopics(parent_topics_id=3, subtopics_name='Fish recipes'),
        Subtopics(parent_topics_id=3, subtopics_name='vegetarian recipes '),
        Subtopics(parent_topics_id=3, subtopics_name='non vegetarian recipes '),
        Subtopics(parent_topics_id=3, subtopics_name=' recipes with eggs '),
        Subtopics(parent_topics_id=3, subtopics_name='Healthy Shakes'),
        Subtopics(parent_topics_id=3, subtopics_name='vegan'),
        Subtopics(parent_topics_id=3, subtopics_name='others'),
        Subtopics(parent_topics_id=4, subtopics_name='bookclubs'),
        Subtopics(parent_topics_id=4, subtopics_name='storyBooks for kindergartener'),
        Subtopics(parent_topics_id=4, subtopics_name='books for Teens'),
        Subtopics(parent_topics_id=4, subtopics_name='Fiction Books'),
        Subtopics(parent_topics_id=4, subtopics_name='NonFiction Books'),
        Subtopics(parent_topics_id=4, subtopics_name='Science Books'),
        Subtopics(parent_topics_id=4, subtopics_name='Painting Books'),
        Subtopics(parent_topics_id=4, subtopics_name='History Books'),
        Subtopics(parent_topics_id=4, subtopics_name='others'),
        Subtopics(parent_topics_id=5, subtopics_name='math'),
        Subtopics(parent_topics_id=5, subtopics_name='Science'),
        Subtopics(parent_topics_id=5, subtopics_name='Algebra'),
        Subtopics(parent_topics_id=5, subtopics_name='Biology'),
        Subtopics(parent_topics_id=5, subtopics_name='middle school'),
        Subtopics(parent_topics_id=5, subtopics_name='High School'),
        Subtopics(parent_topics_id=5, subtopics_name='homeWork'),
        Subtopics(parent_topics_id=5, subtopics_name='others'),
        Subtopics(parent_topics_id=6, subtopics_name='gymnastics'),

        Subtopics(parent_topics_id=6, subtopics_name='roller skate'),
        Subtopics(parent_topics_id=6, subtopics_name='hiking'),
        Subtopics(parent_topics_id=6, subtopics_name='bird watch'),

        Subtopics(parent_topics_id=6, subtopics_name='others'),
        Subtopics(parent_topics_id=7, subtopics_name='others'),
        Subtopics(parent_topics_id=8, subtopics_name='others'),
        Subtopics(parent_topics_id=9, subtopics_name='games'),
        Subtopics(parent_topics_id=9, subtopics_name='story books'),
        Subtopics(parent_topics_id=9, subtopics_name='events'),
        Subtopics(parent_topics_id=9, subtopics_name='series'),
        Subtopics(parent_topics_id=9, subtopics_name='movies'),
        Subtopics(parent_topics_id=9, subtopics_name='others'),
        Subtopics(parent_topics_id=10, subtopics_name='indoor'),
        Subtopics(parent_topics_id=10, subtopics_name='outdoor'),
        Subtopics(parent_topics_id=10, subtopics_name='others'),
        Subtopics(parent_topics_id=11, subtopics_name='others'),
        Subtopics(parent_topics_id=12, subtopics_name='others'),
        Subtopics(parent_topics_id=13, subtopics_name='others'),
        Subtopics(parent_topics_id=14, subtopics_name='pre school'),
        Subtopics(parent_topics_id=14, subtopics_name='kindergarten'),
        Subtopics(parent_topics_id=14, subtopics_name='elementary'),
        Subtopics(parent_topics_id=14, subtopics_name='middle school'),
        Subtopics(parent_topics_id=14, subtopics_name='High school'),
        Subtopics(parent_topics_id=14, subtopics_name='others'),
        Subtopics(parent_topics_id=15, subtopics_name='others'),
        Subtopics(parent_topics_id=15, subtopics_name='middle school'),
        Subtopics(parent_topics_id=15, subtopics_name='High school'),
        Subtopics(parent_topics_id=15, subtopics_name='Elementary school'),
        Subtopics(parent_topics_id=15, subtopics_name='preschool/kindergarten school'),
        Subtopics(parent_topics_id=15, subtopics_name='others'),
        Subtopics(parent_topics_id=16, subtopics_name='others'),
    ]
    )


def create_topics(session):
    print("inserting subtopics ")

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
    # create_establishment(session)
    #create_subtopics(session)

    session.commit()
