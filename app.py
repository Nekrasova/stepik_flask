### Import essential libraries
from flask import Flask, render_template
import random

### Import source data
import static.data as data

application = Flask(__name__)

@application.route('/')
def render_main():
    return render_template('index.html',
                           title=data.title,
                           subtitle=data.subtitle,
                           description=data.description,
                           hotel_list=dict(random.sample(data.tours.items(), 6)),
                           departures=data.departures
                           )

@application.route('/departures/<departure>/')
def render_departure(departure):
    return render_template('departure.html',
                           title=data.title,
                           departures=data.departures,
                           hotel_list=dict(data.tours.items())
                           )

@application.route('/tours/<hotel_id>/')
def render_tours(hotel_id):
    return render_template('tour.html',
                           title=data.title,
                           departures=data.departures,
                           hotel_name=data.tours[int(hotel_id)]['title'],
                           hotel_country=data.tours[int(hotel_id)]['country'],
                           hotel_stars=data.tours[int(hotel_id)]['stars'],
                           hotel_departure=data.departures[data.tours[int(hotel_id)]['departure']],
                           hotel_nights=data.tours[int(hotel_id)]['nights'],
                           hotel_price=data.tours[int(hotel_id)]['price'],
                           hotel_picture=data.tours[int(hotel_id)]['picture'],
                           hotel_description=data.tours[int(hotel_id)]['description']
                           )

@application.route('/booking/')
def render_booking():
    return render_template('booking.html',
                           title=data.title,
                           departures=data.departures
                           )

if __name__ == '__main__':
    application.run()
