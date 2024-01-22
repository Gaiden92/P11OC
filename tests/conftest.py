import pytest

from server import create_app, loadClubs, loadCompetitions


@pytest.fixture
def app():
    app_instance = create_app({"TESTING": True})
    with app_instance.app_context():
        loadClubs(),
        loadCompetitions(),
        yield app_instance

@pytest.fixture
def client(app):    
    with app.test_client() as client:
        yield client






