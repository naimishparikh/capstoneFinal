import os
from sqlalchemy import Column, String, Integer, create_engine, Date, ForeignKey
from flask_sqlalchemy import SQLAlchemy
import json
from flask_migrate import Migrate

# get the required Database environment variables
DB_NAME = os.getenv('DB_NAME', 'castingagency')
DB_USER = os.getenv('DB_USER', 'postgres')
DB_PASSWORD = os.getenv('DB_PASSWORD', '1234')
DB_HOST = os.getenv('DB_HOST', '127.0.0.1')
DB_DIALECT = os.getenv('DB_DIALECT', 'postgresql+psycopg2')
SQLALCHEMY_DATABASE_URI = "{}://{}:{}@{}/{}".format(
    DB_DIALECT, DB_USER, DB_PASSWORD, DB_HOST, DB_NAME)
# database_path = "postgresql://{}/{}".format('localhost:5432', database_name)

db = SQLAlchemy()

'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''


def setup_db(app, database_path=SQLALCHEMY_DATABASE_URI):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    migrate = Migrate(app, db)
    db.init_app(app)
    db.create_all()


'''
Movie table to store title and release date
'''


class Movie(db.Model):
    __tablename__ = 'movies'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    releaseDate = Column(Date)
    actorsmovies = db.relationship('ActorMovie', backref='mov', lazy=True)

    def __init__(self, title, releaseDate):
        self.title = title
        self.releaseDate = releaseDate

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'title': self.title,
            'releaseDate': self.releaseDate,
        }


# Actor table to store actors info such as name,age,gender
class Actor(db.Model):
    __tablename__ = 'actors'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    gender = Column(String)
    actorsmovies = db.relationship('ActorMovie', backref='act', lazy=True)

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age,
            "gender": self.gender
        }


# This table assigns actor to movie and movie to actor
class ActorMovie(db.Model):
    __tablename__ = 'actors_movies'
    id = db.Column(db.Integer, primary_key=True)
    actor_id = Column(Integer, ForeignKey('actors.id'), nullable=False)
    movie_id = Column(Integer, ForeignKey('movies.id'), nullable=False)

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __init__(self, actorId, movieId):
        self.actor_id = actorId
        self.movie_id = movieId

    def format(self):
        return {
            'id': self.id,
            'actor_id': self.actor_id,
            'movie_id': self.movie_id,
        }
