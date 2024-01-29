import pytest

from server import create_app, isCompetitionClose

@pytest.fixture
def app():
    app_instance = create_app({"TESTING": True})
    with app_instance.app_context():
        isCompetitionClose
        yield app_instance

@pytest.fixture
def client(app):    
    with app.test_client() as client:
        with app.app_context():
            yield client