from flask import Flask , render_template
from game_of_life import *

app = Flask(__name__)

@app.route("/")
def index():
    GameOfLife(20, 15)

    return render_template("index.html")

@app.route("/life")
def life():
    world = GameOfLife()
    if world.counter > -1: world.form_new_generation()
    world.counter += 1
    return render_template("life.html" , wld = world)

if __name__ == "__main__":
    app.run()