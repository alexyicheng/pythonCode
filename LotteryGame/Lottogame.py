# 13.11.2024

# Architect of Web-Application
# from flask import Flask
# app = Flask(__name__)
# @app.route('/index')
# def index():
#     return 'Hello!'
# app.run(debug=True)

from flask import Flask,render_template
import random

# create the web-application
app = Flask(__name__)

hero = [
    'Ahri','Akail','Ashe','Master Yi','Soraka','Teemo','Morgana','Olaf'
]

# http://127.0.0.1:5000/index -> http://127.0.0.1: = my own PC & 5000 = my app & index = my created function index()
# app.route() = set up web ressource -> /index =  visit the function index
@app.route('/index')
# create the function index
def index():
    # recall the infos on index.html (index.html has to be in file[templates] otherwise python could find it) -> heros[namelist in html]=hero[herolist] call the single element of the list hero
    return render_template('index.html',heros=hero)

#create the function draw to pick up the hero aus hero-list
@app.route('/draw')
def draw():
    num = random.randint(0,len(hero)-1) # define the range of the HeroList
    return render_template('index.html',heros=hero,h=hero[num])

# start the app
app.run(debug=True)

