def test_message_error_more_twelve_places(client, app, load_clubs_and_competitions_and_bookings):
    data={
        'competition': 'Spring Festival',
        'club': 'Simply Lift',
        'places': '15'
    }

    response = client.post('/purchasePlaces', data=data)

    # Test si la réponse est correcte
    assert response.status_code == 200

    # test si le message d'erreur est bien affiché dans le template.
    assert b'You cannot book more than 12 for one competition, please try again.' in response.data