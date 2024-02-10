import json
from flask import Flask,render_template,request,redirect,flash,url_for
import datetime


def loadClubs():
    with open('clubs.json') as c:
         listOfClubs = json.load(c)['clubs']
         return listOfClubs


def loadCompetitions():
    with open('competitions.json') as comps:
         listOfCompetitions = json.load(comps)['competitions']
         return listOfCompetitions


app = Flask(__name__)
app.secret_key = 'something_special'

competitions = loadCompetitions()
clubs = loadClubs()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/showSummary',methods=['POST'])
def showSummary():
    try:
        club = [club for club in clubs if club['email'] == request.form['email']][0]
        return render_template('welcome.html', club=club, competitions=competitions)
    except IndexError:
        error = "Sorry, that email wasn't found."
        return render_template('index.html', error=error)


@app.route('/book/<competition>/<club>')
def book(competition,club):
    foundClub = [c for c in clubs if c['name'] == club][0]
    foundCompetition = [c for c in competitions if c['name'] == competition][0]
    if foundClub and foundCompetition:
        max_booking_places = int(foundClub['points'])
        competition_date = foundCompetition['date']
        competition_date = datetime.datetime.strptime(competition_date, "%Y-%m-%d %H:%M:%S").date()
        today = datetime.date.today()
        if competition_date >= today:
            if max_booking_places > 12:
                max_booking_places = 12
            return render_template('booking.html',club=foundClub,competition=foundCompetition,
                                   max_booking_places=max_booking_places)
        else:
            flash("This competitions is over.")
    else:
        flash("Something went wrong-please try again")
    return render_template('welcome.html', club=foundClub, competitions=competitions)

@app.route('/purchasePlaces',methods=['POST'])
def purchasePlaces():
    competition = [c for c in competitions if c['name'] == request.form['competition']][0]
    club = [c for c in clubs if c['name'] == request.form['club']][0]
    placesRequired = int(request.form['places'])
    available_points = int(club['points'])
    competition_date = competition['date']
    competition_date = datetime.datetime.strptime(competition_date, "%Y-%m-%d %H:%M:%S").date()
    today = datetime.date.today()
    if competition_date < today:
        flash("This competitions is over.")
    elif placesRequired <= available_points:
        if placesRequired <= 12:
            competition['numberOfPlaces'] = int(competition['numberOfPlaces'])-placesRequired
            club['points'] = int(club['points'])-int(placesRequired)
            flash('Great-booking complete!')
            return render_template('welcome.html', club=club, competitions=competitions)
        else:
            flash("You can't purchase more than 12 places.")
    else:
        flash("The club has not enough available points")
    return render_template('welcome.html', club=club, competitions=competitions)


# TODO: Add route for points display


@app.route('/logout')
def logout():
    return redirect(url_for('index'))

