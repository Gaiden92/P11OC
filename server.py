import json
import datetime
from flask import Flask,render_template,request,redirect,flash,url_for


def loadClubs():
    with open('clubs.json', "r+") as c:
         listOfClubs = json.load(c)['clubs']
         return listOfClubs

def loadCompetitions():
    with open('competitions.json', "r+") as comps:
        listOfCompetitions = json.load(comps)['competitions']
        return listOfCompetitions

def loadBooking():
    with open('bookings.json') as books:
        listBookings = json.load(books)["clubs"]
        return listBookings

def saveClubs(clubs: list):
    with open("clubs.json", "w") as file_clubs:
        clubs_dict = {"clubs":clubs}
        json.dump(clubs_dict, file_clubs, indent=4)

def saveCompetitions(competitions: list):
    with open("competitions.json", "w") as file_competitions:
        competitions_dict = {"competitions": competitions}
        json.dump(competitions_dict, file_competitions, indent=4)

def saveBookings(bookings: list):
        with open("bookings.json", "w") as file_bookings:
            bookings_dict = {"clubs": bookings}
            json.dump(bookings_dict, file_bookings, indent=4)

def create_app(config):
    app = Flask(__name__)
    app.secret_key = 'something_special'

    competitions = loadCompetitions()
    clubs = loadClubs()
    bookings = loadBooking()

    @app.route('/')
    def index():
        return render_template('index.html')

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

        # Mise à jour des points du club, des places de la compétition et du dashboard 
        competition['numberOfPlaces'] = str(int(competition['numberOfPlaces']) - placesRequired)
        club['points'] = str(int(club['points']) - placesRequired)
        bookings[club["name"]][competition["name"]] = str(
            int(
                bookings[club["name"]][competition["name"]]) + placesRequired
                )

        saveClubs(clubs)
        saveCompetitions(competitions)
        saveBookings(bookings)

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