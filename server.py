import json
from flask import Flask,render_template,request,redirect,flash,url_for


def loadClubs():
    with open('clubs.json') as c:
         listOfClubs = json.load(c)['clubs']
         return listOfClubs


def loadCompetitions():
    with open('competitions.json') as comps:
         listOfCompetitions = json.load(comps)['competitions']
         return listOfCompetitions

def loadBooking():
    with open('bookings.json') as books:
        listBookings = json.load(books)
        return listBookings

def update_booking(places_required:int, club:dict, competition:dict) -> bool:
        int_club_points = int(bookings["clubs"][club['name']][competition["name"]])
        int_new_club_points = int_club_points + places_required
        if club_book_more_than_twelve_places(int_new_club_points):
            return False
        else:
            bookings["clubs"][club['name']][competition["name"]] = str(int_new_club_points)
            with open('bookings.json', "w") as file:
                json.dump(bookings, file, indent=4)
                return True
def club_book_more_than_twelve_places(nb_places):
    return nb_places > 12


app = Flask(__name__)
app.secret_key = 'something_special'

competitions = loadCompetitions()
clubs = loadClubs()
bookings = loadBooking()

@app.route('/')
def index():
    bookings = loadBooking()
    return render_template('index.html', bookings=bookings, competitions=competitions)

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

    # Mise à jour des places des clubs par compétitions 
    if update_booking(placesRequired, club, competition):
        flash('Great-booking complete!')
    else:
        flash("You cannot book more than 12 places in the same competition.")
    return render_template('welcome.html', club=club, competitions=competitions)


@app.route('/logout')
def logout():
    return redirect(url_for('index'))