import json, pytest

from ..conftest import create_app, saveClubs, loadClubs

def test_saveClubs(app):
    test_clubs = [
        {"name": "Simply Lift", "email": "john@simplylift.co", "points": "8"},
        {"name": "Iron Temple", "email": "admin@irontemple.com", "points": "2"},
    ]

    saveClubs(test_clubs)
    
    # chargement des données
    loaded_clubs = loadClubs()

    # Vérifiez si les clubs chargés correspondent aux données de test
    assert loaded_clubs == test_clubs