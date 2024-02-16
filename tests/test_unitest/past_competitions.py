from server import app
from tests.conftest import client, mock_competitions, mock_clubs

def test_past_competitiond_valid(mock_clubs, mock_competitions):

    with app.test_client() as client:
        response = client.post('/purchasePlaces', data={'competition' : 'comp 2', 'club' : 'test', 'places': 8})
        assert response.status_code == 200
        data = response.data.decode()
        assert "Number of Places: 7" in data


def test_past_competition_invalid(mock_clubs, mock_competitions):

    with app.test_client() as client:
        response = client.post('/purchasePlaces', data={'competition' : 'comp 1', 'club' : 'test', 'places': 8})
        data = response.data.decode()
        assert "This competitions is over." in data

