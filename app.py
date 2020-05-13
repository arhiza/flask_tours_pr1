from flask import Flask, render_template
from data import *
from random import sample

app = Flask(__name__)

@app.route('/')
def main():
    tours_filtered = {k: tours[k] for k in sample(tours.keys(), 6)} # 6 случайных туров
    return render_template('index.html', title=title, subtitle=subtitle, description=description, departures=departures, tours=tours_filtered)

@app.route('/departures/<departure>')
def show_departure(departure):
    tours_filtered = {}
    for tour_id in tours:
        if tours[tour_id]['departure'] == departure:
            tours_filtered[tour_id] = tours[tour_id]
    return render_template('departure.html', departure=departure, title=title, departures=departures, tours=tours_filtered)

@app.route('/tours/<id>/')
def show_tour(id):
    return render_template('tour.html', tour=tours[int(id)], title=title, departures=departures)


app.run()

