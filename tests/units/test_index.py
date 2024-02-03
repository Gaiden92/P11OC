def test_home_page(client):
    response = client.get('/')
    # test du status code
    assert response.status_code == 200
    # test si le template correspond bien à index.html
    assert b'GUDLFT Registration' in response.data
    
    