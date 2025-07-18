import pytest
from app import app  # ou main

@pytest.fixture
def client():
    app.testing = True
    with app.test_client() as client:
        yield client

def test_home_page(client):
    res = client.get('/')
    assert res.status_code == 200
    assert b'Conversor de Arquivos para PDF' in res.data

def test_converter_route(client):
    # Testa POST vazio (deve falhar ou redirecionar)
    res = client.post('/converter', data={})
    assert res.status_code in [400, 302, 200]  # depende da sua implementação
