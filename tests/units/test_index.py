def test_status_code(client):
    response = client.get('/')
    # test du status code
    assert response.status_code == 200

def test_template(client):
    response = client.get('/')
    # test s'il s'agit du bon template
    assert b'GUDLFT Registration' in response.data
    