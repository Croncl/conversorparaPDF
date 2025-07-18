import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_page(client):
    res = client.get('/')
    assert res.status_code == 200

def test_converter_route_exists(client):
    res = client.get('/converter')
    assert res.status_code != 404

def test_converter_route_post_empty(client):
    res = client.post('/converter', data={})
    # Só garante que não deu 404
    assert res.status_code != 404

def test_converter_route_post_file(client):
    # Arquivo dummy para enviar
    data = {
        'arquivo': (b'teste', 'arquivo.txt')
    }
    res = client.post('/converter', data=data, content_type='multipart/form-data')
    # Só garante que não deu 404
    assert res.status_code != 404
