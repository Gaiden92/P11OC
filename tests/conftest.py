import pytest, json
from flask import template_rendered
from server import ( create_app,
                    saveClubs,
                    loadClubs,
                    saveCompetitions,
                    loadCompetitions,
                    saveBookings,
                    loadBookings,
                    isCompetitionClose
)

@pytest.fixture
def app():
    app_instance = create_app({"TESTING": True})
    with app_instance.app_context():
        loadClubs
        saveClubs
        saveCompetitions
        loadCompetitions
        saveBookings
        loadBookings
        yield app_instance

@pytest.fixture
def client(app):    
    with app.test_client() as client:
        yield client

@pytest.fixture
def clubs_data():
    with open("clubs.json") as file:
        clubs = json.load(file)
        return clubs

@pytest.fixture
def competitions_data():
    with open("competitions.json") as file:
        competitions = json.load(file)
        return competitions

@pytest.fixture
def bookings_data():
    with open("bookings.json") as file:
        bookings = json.load(file)
        return bookings

@pytest.fixture
def load_clubs_and_competitions_and_bookings(app, clubs_data, competitions_data, bookings_data):
    with app.app_context():
        app.club = {
            "name": "Simply Lift",
            "email": "john@simplylift.co",
            "points": "12"
        }
        app.clubs = clubs_data['clubs']
        app.competitions = competitions_data['competitions']
        app.bookings = bookings_data
        app.competition = {
            "name": "Spring Festival",
            "date": "2024-03-27 10:00:00",
            "numberOfPlaces": "18"
        }
        yield

@pytest.fixture
def club_competition_test_open_or_close(app, load_clubs_and_competitions_and_bookings):
    competition_open = [competition for competition in app.competitions
                   if competition['name'] == "Spring Festival"][0]
    competition_close = [competition for competition in app.competitions
                   if competition['name'] == "Fall Classic"][0]

    club = [club for club in app.clubs
                   if club['name'] == "Simply Lift"][0]
    app.club = club
    app.competition_open = competition_open
    app.competition_close = competition_close
    yield



@pytest.fixture
def captured_templates(app):
    recorded = []

    def record(sender, template, context, **extra):
        recorded.append((template, context))

    template_rendered.connect(record, app)
    try:
        yield recorded
    finally:
        template_rendered.disconnect(record, app)