def test_response(client):
    
    response = client.post('/purchasePlaces', data={
        'competition': 'Spring Festival',
        'club': 'Simply Lift',
        'places': '5'
    })

    # Test si la réponse est correcte
    assert response.status_code == 200

def test_success_purchase(client):
    response = client.post('/purchasePlaces', data={
        'competition': 'Spring Festival',
        'club': 'Simply Lift',
        'places': '5'
    })

    # Test si le message de réussite est dans la réponse
    assert b'Great-booking complete!' in response.data  

def test_message_no_booking_more_than_points_available(client):
    response = client.post('/purchasePlaces', data={
        'competition': 'Spring Festival',
        'club': 'Simply Lift',
        'places': '15'
    })
    assert b'You cannot book more places then you got. Please try again.' in response.data

