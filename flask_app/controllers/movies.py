from flask_app import app, render_template, redirect
from flask_app.models.movie import Movie
import random

@app.route('/')
def index():
    Movie.getTop250()
    return render_template('index.html')

@app.route('/play')
def play():
    titles = Movie.getRandTitles()
    return render_template('play.html', plot = Movie.getPlot(random.choice(titles)['id']), titles = titles)

@app.route('/tryagain')
def tryagain():
    Movie.getTop250()
    return redirect('play')

@app.route('/answer/<int:rank>/<string:id>')
def answer(rank, id):
    Movie.checkAnswer(rank, id)
    return redirect('/play')