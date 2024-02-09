from ..conftest import saveBookings, loadBookings

def test_saveBookings(app):
    test_bookings = [
         {
            "name": "Spring Festival",
            "date": "2024-03-27 10:00:00",
            "numberOfPlaces": "18"
        },
        {
            "name": "Fall Classic",
            "date": "2020-10-22 13:30:00",
            "numberOfPlaces": "6"
        }
    ]

    saveBookings(test_bookings)
    
    # chargement des données
    loaded_bookings = loadBookings()

    # Vérifiez si les bookings chargés correspondent aux données de test
    assert loaded_bookings == test_bookings
