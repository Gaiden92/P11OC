from server import loadCompetitions

def test_should_get_competitions(client, app, load_clubs_and_competitions_and_bookings):
    expected_competitions = app.competitions
    competitions = loadCompetitions()
    
    # test du nombre d'élements
    assert len(expected_competitions) == len(competitions)
    # test de la concordance des données
    assert expected_competitions == competitions