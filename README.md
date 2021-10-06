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

https://dev-9a27t4db.us.auth0.com/authorize?audience=actormovie&response_type=token&client_id=guRnBpdib3GwPRFPy6qSoNWuLT4nBgu6&redirect_uri=http://127.0.0.1:5000/actors

AUTH0 information for verifying jwt

AUTH0_DOMAIN = 'dev-9a27t4db.us.auth0.com'
ALGORITHMS = ['RS256']
API_AUDIENCE = 'actormovie'



Installing Python Dependencies
------------------------------
- python version used is Python 3.9.2
- py -m venv env
- .\env\Scripts\activate
- pip install -r requirments.txt
- Install postgres with user 'postgres' and password '1234'
- createdb -Upostgres castingagency
- Install heroku cli
- RUN setup.bat or setup.sh to set up environment variables
- Run the python server locally 
  python app.py
- This will run the flask server at 127.0.0.1:5000
- Run the python unittest suite with the following command
  python test_app.py
- Postman collection for successful case is available in file ActorMovie.postman_collection


