from flask import Flask, request, jsonify, render_template
from requests import get
import urllib.request, json


def index(req):
    url = ('https://api.themoviedb.org/3/movie/popular?api_key=')
    response = get(url)
    data = response.json()
    return [m for m in data["results"]], 200

def show(req, id):
    return find_by_id(id), 200

def find_by_id(id):
    try:
        url = (f'https://api.themoviedb.org/3/movie/{id}?api_key=')
        response = get(url)
        data = response.json()
        return next(movie for movie in movies if movie['id'] == id)
    except:
        return 'error'



























# def index(req):
#     url = ('https://api.themoviedb.org/3/movie/popular?api_key=')
#     response = urllib.request.urlopen(url)
#     data = response.read()
#     dict = json.loads(data)
#     return render_template ("index.html", movies=dict["results"])

# headers = {'user-agent':'my-app/0.0.1'}
