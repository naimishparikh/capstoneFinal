The Casting Agency models a company that is responsible for creating movies and managing and assigning actors to those movies. You are an Executive Producer within the company and are creating a system to simplify and streamline your process.

The application is live and hosted at the following URL on heroku

https://capstoneappnkp10.herokuapp.com/

You can access the following endpoints

Following are the endpoint apis

Endpoints/API behavior
GET /actors and /movies - Get all actors and movies
DELETE /actors/actor_id and /movies/movie_id - Delete the given actor and movie specified with actor id and movie id
POST /actors and /movies and  - Post a new actor or movie
PATCH /actors/actor_id and /movies/movie_id - Update property of an existing actor or movie
POST /actorsmovies  - assign actors to movies. And movies to actors
GET /actorsmovies - get all assigned actors and movies

Following are the RBACs

Roles:
Casting Assistant
    - Can view actors and movies
Casting Director
    - All permissions a Casting Assistant has and…
    - Add or delete an actor from the database
    - Modify actors or movies
Executive Producer
    - All permissions a Casting Director has and…
    - Add or delete a movie from the database
    - Assign movies to actors and actors to movies

Following link will provide you access token in the returned url

https://dev-9a27t4db.us.auth0.com/authorize?audience=actormovie&response_type=token&client_id=guRnBpdib3GwPRFPy6qSoNWuLT4nBgu6&redirect_uri=https://127.0.0.1:5000/actors

I have already setup tokens for different roles above with around 24 hrs lifetime for you to test

AUTH0 information for verifying jwt

AUTH0_DOMAIN = 'dev-9a27t4db.us.auth0.com'
ALGORITHMS = ['RS256']
API_AUDIENCE = 'actormovie'

Executive Producer token
-------------------------

eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImkyVkg4X3ZqOERmdHZrVnY4LS1OeCJ9.eyJpc3MiOiJodHRwczovL2Rldi05YTI3dDRkYi51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjEzYWU3N2E2Mzc2MmMwMDcwYzAwOWM5IiwiYXVkIjoiYWN0b3Jtb3ZpZSIsImlhdCI6MTYzMzQ1Mjc5NCwiZXhwIjoxNjMzNDU5OTk0LCJhenAiOiJndVJuQnBkaWIzR3dQUkZQeTZxU29OV3VMVDRuQmd1NiIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsImRlbGV0ZTptb3ZpZXMiLCJnZXQ6YWN0b3JzIiwiZ2V0OmFjdG9yc21vdmllcyIsImdldDptb3ZpZXMiLCJwYXRjaDphY3RvcnMiLCJwYXRjaDptb3ZpZXMiLCJwb3N0OmFjdG9ycyIsInBvc3Q6YWN0b3JzbW92aWVzIiwicG9zdDptb3ZpZXMiXX0.aY4lidE81dkvumf122q1UR1k35aUyzq-rMGM9aA5J4g1rH8hXtZekjzEwN8HZPmdrgBbsFQAT9KLufYbPY90WptI5V8QWVLwmHuiYk65hH6hpZdkKtd5po7wASz2Aq3ih4Pm-mS7xButZpG48Ob5bhAOpqe4Hn7SachVEW3Niki10Hs7xeOvT7-hGiLAUAjxQsq0Sz6-Fr3CZrbd4En1UKASXrlb7rTDMTbfz_ZyEf5Rf5CyCQ5Uaymh7SVuFeAsD6HIa-TYRQeeLvmklDdZAJ2o4C44-Szrw1roJR1p6i4XRvgQQNGNpC9UeIdu5qeQjjSbSm49SzXeMvxuAIEtBQ

Casting Director token
----------------------

eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImkyVkg4X3ZqOERmdHZrVnY4LS1OeCJ9.eyJpc3MiOiJodHRwczovL2Rldi05YTI3dDRkYi51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjE0MzQwNjFmNDlmMDYwMDcxNmRmMjMyIiwiYXVkIjoiYWN0b3Jtb3ZpZSIsImlhdCI6MTYzMzQ1MzAyNiwiZXhwIjoxNjMzNDYwMjI2LCJhenAiOiJndVJuQnBkaWIzR3dQUkZQeTZxU29OV3VMVDRuQmd1NiIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwicGF0Y2g6YWN0b3JzIiwicGF0Y2g6bW92aWVzIiwicG9zdDphY3RvcnMiXX0.cxMDlYkcypv1BN2eSc2ATN3xQsccesfqQrYhYxYlw0RxnIrp4LRn6DhpC1BxZFU8tvlf6GRRX4qnfOPSbNnr1YlM3lTCljQI7ucpI4I5IFbuCDOKBbVOk-5gR7D1wl9ep-j9YVu2wlTLx5PKfQFDAljnMriQ7ALKhss-fyxZ-lJqfwOPOc7MGLTRTKJJHrJWawOKIQY_FpE8bFE-GHm5P5WyFyNjDruJWhc85bw3lXD7X7lqX5NnaQfzeTaN7rXbzUvSZfYdWFaQLbm3Nv_k4pxOh2v7C9oUde4dpZvzYWLUV_VQhCpRkfmmTyCF3KSf1XVy2kaBaOaZvW3oFoNN7w

Casting Assistant token
-----------------------

eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImkyVkg4X3ZqOERmdHZrVnY4LS1OeCJ9.eyJpc3MiOiJodHRwczovL2Rldi05YTI3dDRkYi51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjE1OTQyZWQ3MmVmYTgwMDY5YzhmNDdkIiwiYXVkIjoiYWN0b3Jtb3ZpZSIsImlhdCI6MTYzMzQ1MzE2OSwiZXhwIjoxNjMzNDYwMzY5LCJhenAiOiJndVJuQnBkaWIzR3dQUkZQeTZxU29OV3VMVDRuQmd1NiIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiXX0.BeLiuC-MWSYCBOT0Bjen2qeA93raRaNhLCluc1oaIlkzC-LCeOo2mmMRMEeW1DD52G5aMAAOrLWpkwQJHcRRYidbUK-_rQTuJ55Jk9I0JuM2KFllteqE9vU88RPWKHo0siSQ3PpryI6DYTma54UJEfCCp3HXBcZk3KfsXhUhufg23Lin0u75ibH2S_wXKOhkiqAkzr5Xu87fXbpHXPI6TSCSqCIjxxGggxGmm61825PkBxY1EinebktmH_b0aEzaT63PByaMia6j2xG5Ed-Oi1j1ub65YTowLLE0BS0hrJya2Bdg947TB_zNYrK--FTAP5aFOo_q_GprY5ba6lQprg


For testing I have also added a postman collection in following file in the main directory with the successful cases

ActorMovie.postman_collection

The unittest library test suite is available in 

test_app.py

Run as :

python test_app.py

-Installing Python Dependencies
 ------------------------------

pip install -r requirments.txt

- Install heroku cli

- Run the python server locally 
  python app.py

- This will run the server at 127.0.0.1:5000
