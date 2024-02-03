from server import loadClubs

def test_should_get_clubs(client):
    expected = [
    {
        "name":"Simply Lift",
        "email":"john@simplylift.co",
        "points":"13"
    },
    {
        "name":"Iron Temple",
        "email": "admin@irontemple.com",
        "points":"4"
    },
    {   "name":"She Lifts",
        "email": "kate@shelifts.co.uk",
        "points":"12"
    }
]

    clubs = loadClubs()

    assert expected == clubs


# tester le nombre de clubs et les noms et emails