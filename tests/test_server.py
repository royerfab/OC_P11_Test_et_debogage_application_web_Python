from server import loadClubs, loadCompetitions, index, showSummary, book, purchasePlaces, logout
import server
import json
from flask import Flask,render_template,request,redirect,flash,url_for
import datetime
import pytest
from tests.conftest import client


def test_loadClubs():
    listOfClubs = json.load(c)['tests']
    expected_value = '[{"info":"info", "autre":"autre", "chiffre":"10"}]'
    assert loadClubs(listOfClubs) == expected_value

def test_loadCompetitions():
    listOfClubs = json.load(c)['tests']
    expected_value = '[{"info":"info", "autre":"autre", "chiffre":"10"}]'
    assert loadCompetitions(listOfClubs) == expected_value


def test_index(client):
    response = client.get('/index')
    assert response.status_code == 200

def test_(client):
	response = client.get('/index')
	data = response.data.decode()
	assert data ==

username = 'testUser'
password = 'testPassword'
client.post('/login', data={'username' : username, 'password' : password})

@pytest.mark.parametrize("competition, club", [(), (), ()])
def test_book(competition, club):
    mocker.patch.object(server, 'club',)
    mocker.patch.object(server, 'competition',)
    club = [{"info":"info", "autre":"autre", "chiffre":"10"}]
    competition = [{"info_2":"info_2", "autre_2":"autre_2", "chiffre_2":"20"}]
    max_booking_places = 14
    competition_date = 2016-12-14
    expected_value = return render_template('booking.html',club=foundClub,competition=foundCompetition,
                                   max_booking_places=max_booking_places)
    assert test_book == expected_value


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

def test_purchasePlaces():
    placesRequired = 13
    available_points = 12
    expected_value = "The club has not enough available points"
    assert test_book == expected_value

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
