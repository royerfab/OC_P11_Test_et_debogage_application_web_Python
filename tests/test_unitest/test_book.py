from server import app
from tests.conftest import client, mock_competitions, mock_clubs


def test_over_invalid(mock_clubs, mock_competitions):

    with app.test_client() as client:
        response = client.get('/book/comp 1/test')
        data = response.data.decode()
        assert "This competitions is over." in data

def test_over_valid(mock_clubs, mock_competitions):

    with app.test_client() as client:
        response = client.get('/book/comp 2/test')
        data = response.data.decode()
        assert "How many places?" in data