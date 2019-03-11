from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Eric'}
    posts = [
        {
            'author': {'username': 'Sarah'},
            'body': 'I like puppies!'
        }, 
        {
            'author': {'username': 'Adam'},
            'body': 'I like Ultimate!'
        },
        {
            'author': {'username': 'Jamison'},
            'body': 'I like airplanes.'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts  )