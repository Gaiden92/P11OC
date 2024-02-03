from server import loadClubs

def test_should_get_clubs(client, app, load_clubs_and_competitions_and_bookings):
    expected_clubs = app.clubs
    clubs = loadClubs()
    
    # test du nombre d'élements
    assert len(expected_clubs) == len(clubs)
    # test de la concordance des données
    assert expected_clubs == clubs
