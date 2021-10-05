import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from app import app
from models import setup_db, Actor, Movie, ActorMovie


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


        #RBAC based authentication. Following are users with the 3 different roles each
        # Replace the tokens accordingly
        self.headersExecutiveProducer = {'Content-Type': 'application/json',
                         'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImkyVkg4X3ZqOERmdHZrVnY4LS1OeCJ9.eyJpc3MiOiJodHRwczovL2Rldi05YTI3dDRkYi51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjEzYWU3N2E2Mzc2MmMwMDcwYzAwOWM5IiwiYXVkIjoiYWN0b3Jtb3ZpZSIsImlhdCI6MTYzMzQ1Mjc5NCwiZXhwIjoxNjMzNDU5OTk0LCJhenAiOiJndVJuQnBkaWIzR3dQUkZQeTZxU29OV3VMVDRuQmd1NiIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsImRlbGV0ZTptb3ZpZXMiLCJnZXQ6YWN0b3JzIiwiZ2V0OmFjdG9yc21vdmllcyIsImdldDptb3ZpZXMiLCJwYXRjaDphY3RvcnMiLCJwYXRjaDptb3ZpZXMiLCJwb3N0OmFjdG9ycyIsInBvc3Q6YWN0b3JzbW92aWVzIiwicG9zdDptb3ZpZXMiXX0.aY4lidE81dkvumf122q1UR1k35aUyzq-rMGM9aA5J4g1rH8hXtZekjzEwN8HZPmdrgBbsFQAT9KLufYbPY90WptI5V8QWVLwmHuiYk65hH6hpZdkKtd5po7wASz2Aq3ih4Pm-mS7xButZpG48Ob5bhAOpqe4Hn7SachVEW3Niki10Hs7xeOvT7-hGiLAUAjxQsq0Sz6-Fr3CZrbd4En1UKASXrlb7rTDMTbfz_ZyEf5Rf5CyCQ5Uaymh7SVuFeAsD6HIa-TYRQeeLvmklDdZAJ2o4C44-Szrw1roJR1p6i4XRvgQQNGNpC9UeIdu5qeQjjSbSm49SzXeMvxuAIEtBQ'}

        self.headersCastingDirector = {'Content-Type': 'application/json',
                         'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImkyVkg4X3ZqOERmdHZrVnY4LS1OeCJ9.eyJpc3MiOiJodHRwczovL2Rldi05YTI3dDRkYi51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjE0MzQwNjFmNDlmMDYwMDcxNmRmMjMyIiwiYXVkIjoiYWN0b3Jtb3ZpZSIsImlhdCI6MTYzMzQ1MzAyNiwiZXhwIjoxNjMzNDYwMjI2LCJhenAiOiJndVJuQnBkaWIzR3dQUkZQeTZxU29OV3VMVDRuQmd1NiIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwicGF0Y2g6YWN0b3JzIiwicGF0Y2g6bW92aWVzIiwicG9zdDphY3RvcnMiXX0.cxMDlYkcypv1BN2eSc2ATN3xQsccesfqQrYhYxYlw0RxnIrp4LRn6DhpC1BxZFU8tvlf6GRRX4qnfOPSbNnr1YlM3lTCljQI7ucpI4I5IFbuCDOKBbVOk-5gR7D1wl9ep-j9YVu2wlTLx5PKfQFDAljnMriQ7ALKhss-fyxZ-lJqfwOPOc7MGLTRTKJJHrJWawOKIQY_FpE8bFE-GHm5P5WyFyNjDruJWhc85bw3lXD7X7lqX5NnaQfzeTaN7rXbzUvSZfYdWFaQLbm3Nv_k4pxOh2v7C9oUde4dpZvzYWLUV_VQhCpRkfmmTyCF3KSf1XVy2kaBaOaZvW3oFoNN7w'}

        self.headersCastingAssistant = {'Content-Type': 'application/json',
                                       'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImkyVkg4X3ZqOERmdHZrVnY4LS1OeCJ9.eyJpc3MiOiJodHRwczovL2Rldi05YTI3dDRkYi51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjE1OTQyZWQ3MmVmYTgwMDY5YzhmNDdkIiwiYXVkIjoiYWN0b3Jtb3ZpZSIsImlhdCI6MTYzMzQ1MzE2OSwiZXhwIjoxNjMzNDYwMzY5LCJhenAiOiJndVJuQnBkaWIzR3dQUkZQeTZxU29OV3VMVDRuQmd1NiIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiXX0.BeLiuC-MWSYCBOT0Bjen2qeA93raRaNhLCluc1oaIlkzC-LCeOo2mmMRMEeW1DD52G5aMAAOrLWpkwQJHcRRYidbUK-_rQTuJ55Jk9I0JuM2KFllteqE9vU88RPWKHo0siSQ3PpryI6DYTma54UJEfCCp3HXBcZk3KfsXhUhufg23Lin0u75ibH2S_wXKOhkiqAkzr5Xu87fXbpHXPI6TSCSqCIjxxGggxGmm61825PkBxY1EinebktmH_b0aEzaT63PByaMia6j2xG5Ed-Oi1j1ub65YTowLLE0BS0hrJya2Bdg947TB_zNYrK--FTAP5aFOo_q_GprY5ba6lQprg'}
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

    #Test cases for executive producer with all permissions

    def test_get_actors(self):
        res = self.client().get('/actors',headers=self.headersExecutiveProducer)
        print("res.data",res.data)
        print("res.data type", type(res.data))
        #binary bytes to string. using ascii decode
        str = b'I am a string'.decode('ASCII')
        print(str)

        bstr = b'I am a b string'

        print("bstr", bstr)

        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['actors']))

    def test_get_actors_failue(self):
        #failure /movie instead of movies
        res = self.client().get('/actor',headers=self.headersExecutiveProducer)
        print("res.data",res.data)
        print("res.data type", type(res.data))
        str = b'I am a string'.decode('ASCII')
        print(str)

        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)




    def test_get_movies(self):
        res = self.client().get('/movies',headers=self.headersExecutiveProducer)
        print("res.data",res.data)
        print("res.data type", type(res.data))
        str = b'I am a string'.decode('ASCII')
        print(str)

        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['movies']))

    def test_get_movies_failue(self):
        #failure /movie instead of movies
        res = self.client().get('/movie',headers=self.headersExecutiveProducer)
        print("res.data",res.data)
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
        res = self.client().patch('/actors/2',json=self.modify_actor_forpatch, headers=self.headersExecutiveProducer)
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
        res = self.client().patch('/movies/2',json=self.modify_movie_forpatch, headers=self.headersExecutiveProducer)
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
        res = self.client().post('/actorsmovies',json=self.actorsmovies, headers=self.headersExecutiveProducer)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['actorsmovies']))

    def test_post_actormovie_failure(self):
        res = self.client().post('/actorsmovie',json=self.actorsmovies, headers=self.headersExecutiveProducer)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)

    def test_get_actormovie(self):
        res = self.client().get('/actorsmovies',headers=self.headersExecutiveProducer)

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


#test cases for Casting Director
    def test_get_actors_cd(self):
        res = self.client().get('/actors',headers=self.headersCastingDirector)
        print("res.data",res.data)
        print("res.data type", type(res.data))

        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['actors']))

    #Casting Director does not have access to get actorsmovies
    def test_get_actormovie_failure_cd(self):
        res = self.client().get('/actorsmovies', headers=self.headersCastingDirector)
        print("after delete actor")
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 403)
        self.assertEqual(data['success'], False)



    #test cases for Casting Assistant
    def test_get_actors_ca(self):
        res = self.client().get('/actors', headers=self.headersCastingAssistant)
        print("res.data", res.data)
        print("res.data type", type(res.data))

        data = json.loads(res.data)

        print("DATA in test get actors",data)

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


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()