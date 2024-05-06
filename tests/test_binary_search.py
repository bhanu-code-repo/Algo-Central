import pytest
from app import create_app

@pytest.fixture
def app():
    app = create_app()
    yield app

@pytest.fixture
def client(app):
    return app.test_client()

# def test_binary_search_iterative(client):
#     data = {
#         "nums": [1, 2, 3, 4, 5, 6, 7, 8, 9],
#         "target": 5
#     }
#     response = client.post('/api/v1/binary-search/iterative', json=data)
#     assert response.status_code == 200
#     assert response.json['message'] == 'Element found at index 4'

#     data = {
#         "nums": [1, 2, 3, 4, 5, 6, 7, 8, 9],
#         "target": 10
#     }
#     response = client.post('/api/v1/binary-search/iterative', json=data)
#     assert response.status_code == 404
#     assert response.json['message'] == 'Element not found in the list'

# def test_binary_search_recursive(client):
#     data = {
#         "nums": [1, 2, 3, 4, 5, 6, 7, 8, 9],
#         "target": 5
#     }
#     response = client.post('/api/v1/binary-search/recursive', json=data)
#     assert response.status_code == 200
#     # assert response.json['message'] == 'Element found at index 4'

#     data = {
#         "nums": [1, 2, 3, 4, 5, 6, 7, 8, 9],
#         "target": 10
#     }
#     response = client.post('/api/v1/binary-search/recursive', json=data)
#     assert response.status_code == 404
#     # assert response.json['message'] == 'Element not found in the list'