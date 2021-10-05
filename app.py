import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from models import db, setup_db, Actor, Movie, ActorMovie
from auth import AuthError, requires_auth


EXTERNAL_IP = os.getenv('EXTERNAL_IP', '127.0.0.1:5000')


def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)
  print("calling setup db")
  setup_db(app)
  print("after setup db")
  CORS(app)

  return app

print("Calling create_app")
app = create_app()

@app.route('/actors', methods=['GET'])
@requires_auth('get:actors')
def get_actors(jwt):
    print("In get Actors")
    actors = Actor.query.order_by(Actor.id).all()
    allActors = []
    for actor in actors:
        allActors.append(actor.format())

    print("Got actors ", allActors)

    return jsonify({
        'success': True,
        'actors': allActors
    })

@app.route('/movies', methods=['GET'])
@requires_auth('get:movies')
def get_movies(jwt):
    print("In get Movies")
    movies = Movie.query.order_by(Movie.id).all()
    allMovies = []
    for movie in movies:
        allMovies.append(movie.format())

    print("Got drinks ", allMovies)

    return jsonify({
        'success': True,
        'movies': allMovies
    })

@app.route('/actors/<int:actor_id>', methods=['DELETE'])
@requires_auth('delete:actors')
def delete_actor(jwt,actor_id):
    try:
        print("in delete actors",actor_id)
        actor = Actor.query.filter(Actor.id == actor_id).one_or_none()
        print("actor ",actor)
        print("actor delete type ",type(actor))
        if actor is None:
            abort(404)

        actor.delete()
        return jsonify({
            'success': True,
             'delete': actor_id
        })
    except Exception as ex:
        print(ex)
        abort(422)

@app.route('/movies/<int:movie_id>', methods=['DELETE'])
@requires_auth('delete:movies')
def delete_movie(jwt,movie_id):
    try:
        print("in delete actors",movie_id)
        movie = Movie.query.filter(Movie.id == movie_id).one_or_none()
        print("drink ",movie)
        print("drink delete type ",type(movie))
        if movie is None:
            abort(404)

        movie.delete()
        return jsonify({
            'success': True,
             'delete': movie_id
        })
    except Exception as ex:
        print(ex)
        abort(422)


@app.route('/actors/<int:actor_id>', methods=['PATCH'])
@requires_auth('patch:actors')
def patch_actor(jwt,actor_id):
    try:
        body = request.get_json()

        name = body.get('name',None)
        age = body.get('age',None)
        gender = body.get('gender',None)
        print("name type",type(name))
        print("age type", type(age))
        print("gender type", type(gender))

        if name is None or age is None or gender is None:
            abort(422)


        actor = Actor.query.filter(Actor.id == actor_id).one_or_none()

        if actor is None:
            abort(404)

        actor.name = name
        actor.age = age
        actor.gender = gender
        actor.update()

        print("In patch after update")
        actors = []
        actors.append(actor.format())
        return jsonify({
            'success': True,
            'actors': actors
        })

    except:
        abort(422)


@app.route('/movies/<int:movie_id>', methods=['PATCH'])
@requires_auth('patch:movies')
def patch_movies(jwt,movie_id):
    try:
        body = request.get_json()

        title = body.get('title',None)
        releaseDate = body.get('releaseDate',None)
        print("releaseDate type", type(title))
        print("releaseDate type",type(releaseDate))
        if title is None or releaseDate is None:
            abort(422)


        movie = Movie.query.filter(Movie.id == movie_id).one_or_none()

        if movie is None:
            abort(404)

        movie.title = title
        movie.releaseDate = releaseDate

        print("movie.releaseDate type", type(movie.releaseDate))
        print("releaseDate type", type(releaseDate))

        movie.update()

        print("In patch after update")
        movies = []
        movies.append(movie.format())
        return jsonify({
            'success': True,
            'movies': movies
        })

    except:
        abort(422)

@app.route('/movies', methods=['POST'])
@requires_auth('post:movies')
def post_movie(jwt):
    body = request.get_json()
    print("body type",type(body))

    title = body.get('title', None)
    releaseDate = body.get('releaseDate', None)
    print("title type", type(title))
    print("releaseDate type", type(releaseDate))

    if title is None or releaseDate is None:
        abort(401)

    movie = Movie(title=title,releaseDate=releaseDate)
    movie.insert()
    movies = []
    movies.append(movie.format())

    return jsonify({
        'success': True,
         'movies': movies
    })


@app.route('/actors', methods=['POST'])
@requires_auth('post:actors')
def post_actor(jwt):
    body = request.get_json()
    print("body type",type(body))

    name = body.get('name', None)
    age = body.get('age', None)
    gender = body.get('gender', None)
    print("In post name type", type(name))
    print("In post age type", type(age))
    print("In post gender type", type(gender))

    if name is None or age is None or gender is None:
        abort(401)

    actor = Actor(name=name,age=age,gender=gender)
    actor.insert()
    actors = []
    actors.append(actor.format())

    return jsonify({
        'success': True,
         'actors': actors
    })


@app.route('/actorsmovies', methods=['POST'])
@requires_auth('post:actorsmovies')
def create_actormovie(jwt):
    # called to create new shows in the db, upon submitting new show listing form
    body = request.get_json()
    print("body type", type(body))

    actor_id = body.get('actor_id', None)
    movie_id = body.get('movie_id', None)

    actorMovie = ActorMovie(actorId=actor_id,movieId=movie_id)

    actorMovie.insert()
    actorsmovies = []
    actorsmovies.append(actorMovie.format())

    return jsonify({
        'success': True,
         'actorsmovies': actorsmovies
    })

@app.route('/actorsmovies', methods=['GET'])
@requires_auth('get:actorsmovies')
def get_actorsmovies(jwt):
    print("In get Movies")
    actorsmovies = ActorMovie.query.order_by(ActorMovie.id).all()
    all = []
    for item in actorsmovies:
        all.append(item.format())

    print("Got actorsmovies ", all)

    return jsonify({
        'success': True,
        'actorsmovies': all
    })


# Error Handling
'''
Example error handling for unprocessable entity
'''



@app.errorhandler(401)
def unauthorized(error):
    print("In unauthorized" , error)
    return jsonify({
        "success": False,
        "error": 401,
        "message": "unauthorized"
    }), 401

@app.errorhandler(403)
def forbidden(error):
    print("In forbidden",error)
    return jsonify({
        "success": False,
        "error": 403,
        "message": "forbidden"
    }), 403


@app.errorhandler(404)
def not_found(error):
    return jsonify({
        "success": False,
        "error": 404,
        "message": "resource not found"
    }), 404


@app.errorhandler(422)
def unprocessable(error):
    print("In unprocessable",error)
    return jsonify({
        "success": False,
        "error": 422,
        "message": "unprocessable"
    }), 422


@app.errorhandler(404)
def bad_request(error):
    print("erorr in bad_Reqest",error)
    return jsonify({
        "success": False,
        "error": 404,
        "message": "bad request"
    }), 404


@app.errorhandler(400)
def bad_request(error):
    print("erorr in bad_Reqest",error)
    return jsonify({
        "success": False,
        "error": 400,
        "message": "bad request"
    }), 400

@app.errorhandler(405)
def not_allowed(error):
    return jsonify({
        "success": False,
        "error": 405,
        "message": "method not allowed"
    }), 405


@app.errorhandler(500)
def internal_server_error(error):
    return jsonify({
        "success": False,
        "error": 500,
        "message": "internal server error"
    }), 500


@app.errorhandler(501)
def not_implemented(error):
    return jsonify({
        "success": False,
        "error": 501,
        "message": "not implemented"
    }), 501


@app.errorhandler(502)
def bad_gateway(error):
    return jsonify({
        "success": False,
        "error": 502,
        "message": "bad gateway"
    }), 502


@app.errorhandler(503)
def service_unavailable(error):
    return jsonify({
        "success": False,
        "error": 503,
        "message": "service unavailable"
    }), 503


@app.errorhandler(504)
def gateway_timeout(error):
    return jsonify({
        "success": False,
        "error": 504,
        "message": "gateway timeout"
    }), 504


@app.errorhandler(505)
def http_version_unsupported(error):
    return jsonify({
        "success": False,
        "error": 505,
        "message": "http version unsupported"
    }), 505

@app.errorhandler(AuthError)
def auth_error(ex):
    print("In auth error")
    response = jsonify(ex.error)
    response.status_code = ex.status_code
    return response



if __name__ == '__main__':
    app.run(host=EXTERNAL_IP, port=5000, debug=True)