from ..conftest import create_app, saveCompetitions, loadCompetitions

def test_saveCompetitions(app):
    test_competitions = [
         {
            "name": "Spring Festival",
            "date": "2024-03-27 10:00:00",
            "numberOfPlaces": "18"
        },
        {
            "name": "Fall Classic",
            "date": "2020-10-22 13:30:00",
            "numberOfPlaces": "5"
        }
    ]

    saveCompetitions(test_competitions)
    
    # chargement des données
    loaded_competitions = loadCompetitions()

    # Vérifiez si les competitions chargés correspondent aux données de test
    assert loaded_competitions == test_competitions
