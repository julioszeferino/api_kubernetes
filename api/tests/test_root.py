from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_quando_requisitar_raiz_entao_retorna_mensagem() -> None:
    response = client.get('/')
    assert response.status_code == 200
    assert response.json() == {'message': 'API Cronos'}