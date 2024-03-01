from server import app
from tests.conftest import client, mock_competitions, mock_clubs


def test_booking_places_valid(mock_clubs, mock_competitions):

    with app.test_client() as client:
        email = 'test@test.com'
        response = client.post('/showSummary', data={'email' : email})
        assert response.status_code == 200
        data = response.data.decode()
        assert "Welcome, test@test.com" in data
        assert "Number of Places: 15" in data
        assert "Points available: 15" in data

        response = client.post('/purchasePlaces', data={'competition': 'comp 2', 'club': 'test', 'places': 8})
        assert response.status_code == 200
        data = response.data.decode()
        assert "Number of Places: 7" in data
        assert "Points available: 7" in data

def test_more_twelve_points_valid(mock_clubs, mock_competitions):

    with app.test_client() as client:
        email = 'test@test.com'
        response = client.post('/showSummary', data={'email' : email})
        assert response.status_code == 200
        data = response.data.decode()
        assert "Welcome, test@test.com" in data
        assert "Number of Places: 15" in data
        assert "Points available: 15" in data

        response = client.post('/purchasePlaces', data={'competition': 'comp 2', 'club': 'test', 'places': 13})
        assert response.status_code == 200
        data = response.data.decode()
        assert "Number of Places: 15" in data
        assert "Points available: 15" in data

