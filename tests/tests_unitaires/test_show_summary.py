import pytest

from  tests.conftest import client, loadCompetitions, loadClubs


def test_should_find_a_club(client, user):
    clubs = loadClubs()
    club = [club for club in clubs if club['email'] == data['email']][0]
    assert club == {'email': data['email'], 'name': 'She Lifts', 'points': '12'}

def test_should_raise_index_error_exception(client):
    clubs = loadClubs()
    with pytest.raises(IndexError):
        club = [club for club in clubs if club['email'] == ""][0]

