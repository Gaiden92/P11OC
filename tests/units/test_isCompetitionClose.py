from tests.conftest import isCompetitionClose


def test_saveCompetitions(app):
    competition_date = "2024-03-27 10:00:00"
    close = isCompetitionClose(competition_date)
    expected = False

    # Vérifiez si la compétition est clôturée
    assert close == expected