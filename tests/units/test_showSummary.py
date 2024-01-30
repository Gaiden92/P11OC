def test_message_success(client):
    response = client.post('/showSummary', data={
        'email': 'john@simplylift.co'
    })

    # Test si la réponse est correcte
    assert b'You are now connect' in response.data

def test_message_email_error(client):
    response = client.post('/showSummary', data={
        'email': 'hello'
    })
    with client.session_transaction() as session:
        flash_messages = dict(session['_flashes'])

    # Test si le message d'erreur est bien dans le dictionnaire flash_messages
    assert flash_messages['message'] == 'You need to enter a valid email. Please try again.'

def test_status_code(client):
    response = client.post('/showSummary', data={
        'email': 'john@simplylift.co'
    })
    assert response.status_code == 200