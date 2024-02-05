import pytest
from server import create_app

def test_logout(client, app, load_clubs_and_competitions_and_bookings):
    
    response = client.get('/logout')
    
    assert response.status_code == 302  
    assert response.location == 'http://localhost/' 

    # Test de la réinitialisation des données 
    assert not hasattr(client, "clubs") 
    assert not hasattr(client, "competitions") 