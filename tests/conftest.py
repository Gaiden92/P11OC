import pytest, json
from server import create_app

@pytest.fixture
def app():
    app_instance = create_app({"TESTING": True})
    with app_instance.app_context():
        yield app_instance

@pytest.fixture
def client(app):    
    with app.test_client() as client:
        with app.app_context():
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
    return {
        "clubs": {
            "She Lifts": {
                "Spring Festival": "12",
                "Fall Classic": "2"
            },
            "Iron Temple": {
                "Spring Festival": "10",
                "Fall Classic": "5"
            },
            "Simply Lift": {
                "Spring Festival": "1",
                "Fall Classic": "9"
            }
        }
}


@pytest.fixture
def load_clubs_and_competitions_and_bookings(app, clubs_data, competitions_data, bookings_data):
    with app.app_context():
        app.clubs = clubs_data['clubs']
        app.competitions = competitions_data['competitions']
        app.bookings = bookings_data['clubs']
        yield
