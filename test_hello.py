from hello import app

def test_hello():
    response = app.test_client().get('/')

    assert response.status_code == 200
    assert response.data == b'Hello, World!'

def test_add():
	response = app.test_client().get('/add/2/3')

	assert response.status_code == 200
	assert response.data == b'5'