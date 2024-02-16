import pytest

from server import app


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

@pytest.fixture
def mock_competitions(mocker):
    competitions = [
        {
            "name": "comp 1",
            "date": "2019-05-01 10:00:00",
            "numberOfPlaces": "20"
        },
        {
            "name": "comp 2",
            "date": "2025-01-01 13:30:00",
            "numberOfPlaces": "15"
        }
    ]
    mocker.patch("server.competitions", competitions)
    return competitions

@pytest.fixture
def mock_clubs(mocker):
    clubs = [
    {
        "name":"test",
        "email":"test@test.com",
        "points":"15"
    },
    {
        "name":"admin_test",
        "email": "admin_test@admin_test.com",
        "points":"4"
    },
    {   "name":"test_2",
        "email": "test_2@test_2.com",
        "points":"12"
    }
    ]
    mocker.patch("server.clubs", clubs)
    return clubs