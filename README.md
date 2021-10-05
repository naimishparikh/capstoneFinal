The Casting Agency models a company that is responsible for creating movies and managing and assigning actors to those movies. You are an Executive Producer within the company and are creating a system to simplify and streamline your process.

-Installing Python Dependencies
 ------------------------------

pip install -r requirments.txt

- Install heroku cli

- Run the python server locally 
  python app.py

- This will run the server at 127.0.0.1:5000

Following are the endpoint apis

Endpoints/API behavior
GET /actors and /movies - Get all actors and movies
DELETE /actors/ and /movies/ - Delete the given actor and movie specified with actor id and movie id
POST /actors and /movies and  - Post a new actor or movie
PATCH /actors/ and /movies/ - Update property of an existing actor or movie
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