import uuid
import datetime

from main import db
from main.model.favorite import Favorites


def get_all_favByUserId(Id):
    return Favorites.query.filter_by(follower_id=Id).first()
