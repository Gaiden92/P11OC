def test_purchasesPlaces(client, app, load_clubs_and_competitions_and_bookings):
    data = {
        'competition': 'Spring Festival',
        'club': 'Simply Lift',
        'places': '5'
    }
    response = client.post('/purchasePlaces', data=data)

    club = [club for club in app.clubs if club["name"] == data['club']][0]
    competition = [
        competition for competition in app.competitions 
        if competition['name'] == data["competition"]][0]
    
    # Test si la réponse est correcte
    assert response.status_code == 200
    # Test si le message de réussite est dans la réponse
    assert b'Great-booking complete!' in response.data

    # test du calcul du nombre de place restants de la compétition
    new_places = int(competition['numberOfPlaces']) - int(data['places'])
    assert f'Number of Places: {str(new_places)}' in response.data.decode()

def test_message_no_booking_more_than_points_available(client):
    response = client.post('/purchasePlaces', data={
        'competition': 'Spring Festival',
        'club': 'Simply Lift',
        'places': '15'
    })
    # Test si la réponse est correcte
    assert response.status_code == 200
    assert b'You cannot book more places then you got. Please try again.' in response.data

