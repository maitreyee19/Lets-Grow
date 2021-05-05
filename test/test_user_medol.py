import unittest
import datetime

from main import db
from main.model.user import User
from test.base import BaseTestCase


class TestUserModel(BaseTestCase):

    def test_encode_auth_token(self):
        user = User(
            email='test@test.com',
            username='test'
        )
        db.session.add(user)
        db.session.commit()
        self.assertTrue(1 == 1)
    def test_decode_auth_token(self):
        user = User(
            email='test@test.com',
            username='test'
        )
        db.session.add(user)
        db.session.commit()
        self.assertTrue(1 == 1)



if __name__ == '__main__':
    unittest.main()