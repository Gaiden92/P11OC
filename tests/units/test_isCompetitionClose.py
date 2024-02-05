from tests.conftest import isCompetitionClose, app, client, club_competition_test_open_or_close


def test_book_competition_open(client, app, club_competition_test_open_or_close):
    club = app.club
    competition = app.competition_open
    response = client.get(f'/book/{competition["name"]}/{club["name"]}')
    competition_date = competition["date"]
    is_close = isCompetitionClose(competition_date)

    # Test du status code
    assert response.status_code == 200
    # Vérifiez si la compétition est clôturée
    assert is_close == False

def test_book_competition_close(client, app, club_competition_test_open_or_close):
    club = app.club
    competition = app.competition_close
    response = client.get(f'/book/{competition["name"]}/{club["name"]}')
    competition_date = competition["date"]
    is_close = isCompetitionClose(competition_date)

    # Test du status code
    assert response.status_code == 200
    # Vérifiez si la compétition est clôturée
    assert is_close == True

    # # Test des données attendues sur la page book
    assert competition["name"] in response.data.decode()
    assert club["name"] in response.data.decode()

