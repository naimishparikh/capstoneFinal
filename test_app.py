import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from app import app
from models import setup_db, Actor, Movie, ActorMovie

# TOKENS FROM ENVIRONMENT VARIABLES
PRODUCER = os.getenv('PRODUCER')
DIRECTOR = os.getenv('DIRECTOR')
ASSISTANT = os.getenv('ASSISTANT')


class ActorsMoviesTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        print("Calling create_app in unittest")

        self.app = app
        self.client = self.app.test_client
        self.database_name = "castingagency"
        self.database_path = "postgresql://{}:{}@{}/{}".format('postgres',
                                                               '1234',
                                                               'localhost:5432',
                                                               self.database_name)
        setup_db(self.app, self.database_path)

        self.new_actor = {
            "name": "nkp1",
            "age": 42,
            "gender": "male"
        }

        self.new_movie = {
            "title": "movie1",
            "releaseDate": "2012-05-02"
        }

        self.modify_actor_forpatch = {
            "name": "nkp1",
            "age": 42,
            "gender": "male"
        }

        self.modify_movie_forpatch = {
            "title": "movie12",
            "releaseDate": "2012-05-02"
        }

        self.actorsmovies = {
            "actor_id": 2,
            "movie_id": 2
        }

        # RBAC based authentication. Following are users with the 3 different roles each
        # Replace the tokens accordingly
        str_token = 'Bearer ' + PRODUCER
        self.headersExecutiveProducer = {'Content-Type': 'application/json',
                                         'Authorization': str_token}

        str_token = 'Bearer ' + DIRECTOR
        self.headersCastingDirector = {'Content-Type': 'application/json',
                                         'Authorization': str_token}

        #str_token = 'Bearer ' + ASSISTANT
        #self.headersCastingAssistant = {'Content-Type': 'application/json',
        #                                 'Authorization': str_token}

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

    def tearDown(self):
        """Executed after reach test"""
        pass

    """
    TODO
    Write at least one test for each test for successful operation and for expected errors.
    """

    # Test cases for executive producer with all permissions

    def test_get_actors(self):
        res = self.client().get('/actors', headers=self.headersExecutiveProducer)
        print("res.data", res.data)
        print("res.data type", type(res.data))
        # binary bytes to string. using ascii decode
        str = b'I am a string'.decode('ASCII')
        print(str)

        bstr = b'I am a b string'

        print("bstr", bstr)

        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['actors']))

    def test_get_actors_failue(self):
        # failure /movie instead of movies
        res = self.client().get('/actor', headers=self.headersExecutiveProducer)
        print("res.data", res.data)
        print("res.data type", type(res.data))
        str = b'I am a string'.decode('ASCII')
        print(str)

        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)

    def test_get_movies(self):
        res = self.client().get('/movies', headers=self.headersExecutiveProducer)
        print("res.data", res.data)
        print("res.data type", type(res.data))
        str = b'I am a string'.decode('ASCII')
        print(str)

        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['movies']))

    def test_get_movies_failue(self):
        # failure /movie instead of movies
        res = self.client().get('/movie', headers=self.headersExecutiveProducer)
        print("res.data", res.data)
        print("res.data type", type(res.data))
        str = b'I am a string'.decode('ASCII')
        print(str)

        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)

    def test_post_movie(self):
        res = self.client().post('/movies', json=self.new_movie, headers=self.headersExecutiveProducer)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['movies']))

    def test_post_movie_failure(self):
        res = self.client().post('/movie', json=self.new_movie, headers=self.headersExecutiveProducer)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)

    def test_post_actor(self):
        res = self.client().post('/actors', json=self.new_actor, headers=self.headersExecutiveProducer)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['actors']))

    def test_post_actor_failure(self):
        res = self.client().post('/actor', json=self.new_actor, headers=self.headersExecutiveProducer)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)

    def test_delete_actor(self):
        res = self.client().delete('/actors/12', headers=self.headersExecutiveProducer)
        print("after delete actor")
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['delete'])

    def test_delete_actor_failure(self):
        res = self.client().delete('/movie', headers=self.headersExecutiveProducer)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)

    def test_delete_movie(self):
        res = self.client().delete('/movies/12', headers=self.headersExecutiveProducer)
        print("after delete actor")
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['delete'])

    def test_delete_actor_failure(self):
        res = self.client().delete('/movie', headers=self.headersExecutiveProducer)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)

    def test_patch_actor(self):
        res = self.client().patch('/actors/2', json=self.modify_actor_forpatch, headers=self.headersExecutiveProducer)
        print("after delete actor")
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['actors']))

    def test_patch_actor_failure(self):
        res = self.client().patch('/actor', headers=self.headersExecutiveProducer)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)

    def test_patch_movie(self):
        res = self.client().patch('/movies/2', json=self.modify_movie_forpatch, headers=self.headersExecutiveProducer)
        print("after delete actor")
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['movies']))

    def test_patch_movie_failure(self):
        res = self.client().patch('/movie', headers=self.headersExecutiveProducer)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)

    def test_post_actormovie(self):
        res = self.client().post('/actorsmovies', json=self.actorsmovies, headers=self.headersExecutiveProducer)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['actorsmovies']))

    def test_post_actormovie_failure(self):
        res = self.client().post('/actorsmovie', json=self.actorsmovies, headers=self.headersExecutiveProducer)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)

    def test_get_actormovie(self):
        res = self.client().get('/actorsmovies', headers=self.headersExecutiveProducer)

        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['actorsmovies']))

    def test_get_actormovie_failure(self):
        res = self.client().get('/actorsmovie', headers=self.headersExecutiveProducer)
        print("after delete actor")
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)

    # test cases for Casting Director
    def test_get_actors_cd(self):
        res = self.client().get('/actors', headers=self.headersCastingDirector)
        print("res.data", res.data)
        print("res.data type", type(res.data))

        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['actors']))

    # Casting Director does not have access to get actorsmovies
    def test_get_actormovie_failure_cd(self):
        res = self.client().get('/actorsmovies', headers=self.headersCastingDirector)
        print("after delete actor")
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 403)
        self.assertEqual(data['success'], False)

'''
    # test cases for Casting Assistant
    def test_get_actors_ca(self):
        res = self.client().get('/actors', headers=self.headersCastingAssistant)
        print("res.data", res.data)
        print("res.data type", type(res.data))

        data = json.loads(res.data)

        print("DATA in test get actors", data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['actors']))

    # Casting Assistant does not have access to get actorsmovies
    def test_get_actormovie_failure_ca(self):
        res = self.client().get('/actorsmovies', headers=self.headersCastingAssistant)
        print("after delete actor")
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 403)
        self.assertEqual(data['success'], False)
'''

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
