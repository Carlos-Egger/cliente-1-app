import pytest
from app.main import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_listar_livros(client):
    response = client.get('/livros')
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)
    assert any(livro['titulo'] == '1984' for livro in data)
