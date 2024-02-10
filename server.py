import datetime, json
from flask import Flask,render_template,request,redirect,flash,url_for


def loadClubs():
    with open('clubs.json', "r+") as c:
         listOfClubs = json.load(c)['clubs']
         return listOfClubs

def loadCompetitions():
    with open('competitions.json', "r+") as comps:
        listOfCompetitions = json.load(comps)['competitions']
        return listOfCompetitions

def loadBookings():
    with open('bookings.json') as books:
        listBookings = json.load(books)
        return listBookings

def saveClubs(clubs: list):
    with open("clubs.json", "w") as file_clubs:
        clubs_dict = {"clubs":clubs}
        json.dump(clubs_dict, file_clubs, indent=4)

def saveCompetitions(competitions: list):
    with open("competitions.json", "w") as file_competitions:
        competitions_dict = {"competitions": competitions}
        json.dump(competitions_dict, file_competitions, indent=4)

def saveBookings(bookings: dict):
        with open("bookings.json", "w") as file_bookings:
            
            json.dump(bookings, file_bookings, indent=4)

def isCompetitionClose(date_competition):
    actualDate = datetime.datetime.now()
    dateCompetition = datetime.datetime.strptime(date_competition, "%Y-%m-%d %H:%M:%S")

    return actualDate > dateCompetition

def create_app(config):
    app = Flask(__name__, static_url_path='/static')
    app.secret_key = 'something_special'

    competitions = loadCompetitions()
    clubs = loadClubs()
    bookings = loadBookings()

    @app.route('/')
    def index():
        bookings = loadBookings()
        return render_template('index.html', competitions=competitions, bookings=bookings)

    @app.route('/showSummary',methods=['POST'])
    def showSummary():
        # Tester si l'email existe en base de donnée
        try:
            club = [club for club in clubs if club['email'] == request.form['email']][0]
        except IndexError:
            flash('You need to enter a valid email. Please try again.')
            return redirect(url_for('index'))
        flash("You are now connect")
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

        pointsClub = int(club['points'])

        # tester que le nombre de place reservées n'est pas supérieur au points du club 
        if pointsClub - placesRequired < 0:
            flash('You cannot book more places then you got. Please try again.')
            return render_template('booking.html',club=club,competition=competition)
        
        # Tester que le nombre de places reservées ne soient pas supérieurs à 12.
        elif placesRequired + int(nb_places) > 12:
            flash("You cannot book more than 12 for one competition, please try again.")
            return render_template('booking.html', club=club, competition= competition)
        
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


    @app.route('/logout')
    def logout():
        return redirect(url_for('index'))
    
    return app

if __name__ == "__main__":
    app = create_app({"TESTING": True, "PORT": 5000})
    app.run(debug=True)