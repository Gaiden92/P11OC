import pytest

def test_showSummary(client, app, load_clubs_and_competitions_and_bookings):
    # Test exception non levée
    try:
        client.post('/showSummary', data={"email": "invalid@email.com"})
    except IndexError:
        pytest.fail('Unexpected IndexError was raised')

    with client.session_transaction() as session:
        flash_messages = dict(session.get('_flashes', []))
        assert flash_messages['message'] == 'You need to enter a valid email. Please try again.'

    response = client.post('/showSummary', data={
        'email': 'john@simplylift.co'
    })

    # test status code
    assert response.status_code == 200

    # Test si la réponse est correcte
    assert b'You are now connect' in response.data
    club = [club for club in app.clubs if club['email'] == 'john@simplylift.co'][0]
    assert club['email'] in response.data.decode()
    assert club['points'] in response.data.decode()


def test_message_email_error(client):
    response = client.post('/showSummary', data={
        'email': 'hello'
    })
    with client.session_transaction() as session:
        flash_messages = dict(session['_flashes'])

    # Test si le message d'erreur est bien dans le dictionnaire flash_messages
    assert flash_messages['message'] == 'You need to enter a valid email. Please try again.'