from flask import Flask, request, jsonify, render_template
from controllers import movies
from flask_cors import CORS
from werkzeug import exceptions
import os

app = Flask(__name__)
CORS(app)

@app.route('/')
def welcome():
    return render_template('index.html', title=f'Movie App')

@app.route('/movies', methods = ['GET'])
def movies_handler():
    data = movies.index(request)
    movie =[]
    for m in data[0]:
        m = {
            'title': m['title'],
            'overview': m['overview'],
            'backdrop_path': m['backdrop_path']
        }
        if m['backdrop_path'] != None: 
            movie.append(m)
    return render_template('index.html', data = movie)

@app.route('/movies/<int:movie_id>', methods = ['GET'])
def movie_handler(movie_id):
    resp, code = movies.show(request, movie_id)
    return jsonify(resp), code

if __name__ == '__main__':
    app.run(debug=True)





















 #url = ('https://api.themoviedb.org/3/movie/popular?api_key=3e75bf46bc720cd7c4d444e109c461d9')
    # response = urllib.request.urlopen(url)
    # data = response.read()
    # dict = json.loads(data)
    # return render_template ("index.html", movies=dict["results"])
    
    # # fns = {
    # #     'GET': movies.index,
    # #     'POST': movies.create
    # # }
