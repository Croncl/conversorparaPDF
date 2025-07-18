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

def test_converter_route_empty_post(client):
    res = client.post('/converter', data={})
    assert res.status_code in [400, 302, 200]

def test_converter_route_with_file(client):
    # Cria um arquivo em memória (PNG simples 1x1 pixel)
    data = {
        'arquivo': (io.BytesIO(b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x01'
                              b'\x00\x00\x00\x01\x08\x02\x00\x00\x00\x90wS\xde\x00'
                              b'\x00\x00\nIDATx\xdac\xfc\xff\xff?\x00\x05\xfe\x02'
                              b'\xfeA\x1d\x8d\x9c\x00\x00\x00\x00IEND\xaeB`\x82'), 'test.png')
    }
    res = client.post('/converter', data=data, content_type='multipart/form-data')
    # Espera 200 se converteu ok, ou pode ajustar conforme seu código
    assert res.status_code == 200
    # Pode checar se a resposta contém algo esperado (ex: link para download, texto, etc)
    assert b'PDF' in res.data or b'pdf' in res.data
