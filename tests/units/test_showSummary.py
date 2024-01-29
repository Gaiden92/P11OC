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

    assert flash_messages['message'] == 'You need to enter a valid email. Please try again.'