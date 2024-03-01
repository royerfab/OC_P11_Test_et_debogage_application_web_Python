from server import app
from tests.conftest import client, mock_competitions, mock_clubs


def test_points_display_invalid(mock_clubs, mock_competitions):
    with app.test_client() as client:
        email = 'test@test.com'
        response = client.post('/showSummary', data={'email' : email})
        assert response.status_code == 200
        data = response.data.decode()
        assert "Welcome, test@test.com" in data

def test_points_display_valid(mock_clubs, mock_competitions):

    with app.test_client() as client:
        response = client.get('/points_display')
        assert response.status_code == 200
        data = response.data.decode()
        assert "Clubs:" in data