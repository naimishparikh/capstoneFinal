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
