def test_hello(client):
    response = client.get('/api/status')
    assert response.status_code == 200
    assert response.json == {"message": "Ok"}