import json
import datetime
from flask import Flask,render_template,request,redirect,flash,url_for


def loadClubs():
    with open('clubs.json') as c:
         listOfClubs = json.load(c)['clubs']
         return listOfClubs

def loadCompetitions():
    with open('competitions.json') as comps:
         listOfCompetitions = json.load(comps)['competitions']
         return listOfCompetitions
<<<<<<< HEAD
    
def loadBookings():
    with open('bookings.json') as file:
        listBookings = json.load(file)
        return listBookings

def isCompetitionClose(date_competition):
    actualDate = datetime.datetime.now()
    dateCompetition = datetime.datetime.strptime(date_competition, "%Y-%m-%d %H:%M:%S")

    return actualDate > dateCompetition
=======

def loadBookings():
    with open("bookings.json") as books:
        listOfBookings = json.load(books)
        return listOfBookings
    
# Vérification du nombre de places déjà reservées pour une même compétition
def club_book_more_than_twelve_places(nb_places):
    return nb_places > 12
>>>>>>> bug/clubs_shouldn't_be_able_to_book_more_than_12_places_per_competition

def create_app(config):
    app = Flask(__name__)
    app.secret_key = 'something_special'

    competitions = loadCompetitions()
    clubs = loadClubs()

    @app.route('/')
    def index():
        return render_template('index.html', competitions=competitions)

    @app.route('/showSummary',methods=['POST'])
    def showSummary():
        club = [club for club in clubs if club['email'] == request.form['email']][0]
        return render_template('welcome.html',club=club,competitions=competitions)


    @app.route('/book/<competition>/<club>')
    def book(competition,club):
        foundClub = [c for c in clubs if c['name'] == club][0]
        foundCompetition = [c for c in competitions if c['name'] == competition][0]
        if foundClub and foundCompetition:
            return render_template('booking.html',club=foundClub,competition=foundCompetition)
        else:
            flash("Something went wrong-please try again")
            return render_template('welcome.html', club=club, competitions=competitions)


    @app.route('/purchasePlaces',methods=['POST'])
    def purchasePlaces():
        competition = [c for c in competitions if c['name'] == request.form['competition']][0]
        club = [c for c in clubs if c['name'] == request.form['club']][0]
        placesRequired = int(request.form['places'])
        
        # tester si la compétition est déja clôturée 
        if isCompetitionClose(competition['date']):
            flash('You cannot book places for a competition close.')
            return render_template('booking.html',club=club,competition=competition)
        bookings = loadBookings()
        nb_places = bookings[club["name"]][competition["name"]]

        placesRequired = int(request.form['places'])

        # Tester que le nombre de places reservées ne soient pas supérieurs à 12.
        if placesRequired + int(nb_places) > 12:
            flash("You cannot book more than 12 for one competition, please try again.")
            return render_template('booking.html', club=club, competition= competition)
        
        competition['numberOfPlaces'] = int(competition['numberOfPlaces'])-placesRequired
        flash('Great-booking complete!')
        return render_template('welcome.html', club=club, competitions=competitions)


    # TODO: Add route for points display


    @app.route('/logout')
    def logout():
        return redirect(url_for('index'))
    
    return app

if __name__ == "__main__":
    app = create_app({"TESTING": True})
    app.run(debug=True)