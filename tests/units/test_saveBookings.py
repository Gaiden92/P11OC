from ..conftest import saveBookings, loadBookings

def test_saveBookings(app):
    test_bookings = {
        "She Lifts": {
            "Spring Festival": "1",
            "Fall Classic": "2"
        },
        "Iron Temple": {
            "Spring Festival": "10",
            "Fall Classic": "5"
        },
        "Simply Lift": {
            "Spring Festival": "5",
            "Fall Classic": "9"
        }
    }

    saveBookings(test_bookings)
    
    # chargement des données
    loaded_bookings = loadBookings()

    # Vérifiez si les bookings chargés correspondent aux données de test
    assert loaded_bookings == test_bookings
