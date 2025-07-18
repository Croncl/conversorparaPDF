import io
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
    assert b'Conversor de Arquivos para PDF' in res.data

def test_post_empty(client):
    res = client.post('/', data={})
    # Se não enviar arquivo, o app redireciona (302)
    assert res.status_code == 302

def test_post_file_not_allowed_extension(client):
    data = {
        'file': (io.BytesIO(b'teste'), 'arquivo.txt')  # txt não permitido
    }
    res = client.post('/', data=data, content_type='multipart/form-data')
    # O app deve redirecionar (302) com flash porque extensão não é permitida
    assert res.status_code == 302

def test_post_file_allowed_extension(client):
    data = {
        'file': (io.BytesIO(b'teste'), 'arquivo.png')  # png permitido
    }
    res = client.post('/', data=data, content_type='multipart/form-data')
    # Dependendo da implementação do app, pode ser sucesso (200) ou redirecionamento (302)
    assert res.status_code in (200, 302)
