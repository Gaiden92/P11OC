import pytest
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
    return {
        "clubs": [
            {
                "name": "Simply Lift",
                "email": "john@simplylift.co",
                "points": "13"
            },
            {
                "name": "Iron Temple",
                "email": "admin@irontemple.com",
                "points": "4"
            }
        ]
    }

@pytest.fixture
def competitions_data():
    return {
        "competitions": [
            {
                "name": "Spring Festival",
                "date": "2020-03-27 10:00:00",
                "numberOfPlaces": "25"
            },
            {
                "name": "Fall Classic",
                "date": "2020-10-22 13:30:00",
                "numberOfPlaces": "13"
            }
        ]
    }

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
