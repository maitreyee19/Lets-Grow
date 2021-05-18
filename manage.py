import os
import unittest


from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from main import create_app, db
from main.model import User, Post
from sql_scripts import create_ageGroup,create_establishment,create_topics

app = create_app(os.getenv('BOILERPLATE_ENV') or 'dev')

app.app_context().push()

manager = Manager(app)

migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)


@manager.command
def run():
    app.run()


@manager.command
def test():
    """Runs the unit tests."""
    tests = unittest.TestLoader().discover('test', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1


@manager.command
def seed():
    """Add seed data to the database."""
    db.create_all()
    # john = User(username='Lony Das', email='abc@xyz.com')
    # post = Post()
    # post.title = "Story time at Libray"
    # post.body = "This is the first post"
    # post.author = john
    # db.session.add(post)
    # db.session.add(john)
    # db.session.commit()
    # print(User.query.all())
    # print(Post.query.all())
    #create_ageGroup(db.session)
    #create_establishment(db.session)
    create_topics(db.session)
    db.session.commit()



if __name__ == '__main__':
    manager.run()

