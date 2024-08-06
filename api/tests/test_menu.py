from fastapi.testclient import TestClient
from ..controllers import menu as controller
from ..main import app
import pytest
from ..models import menu as model

# Create a test client for the app
client = TestClient(app)


@pytest.fixture
def db_session(mocker):
    return mocker.Mock()


def test_create_menu(db_session):
    # Create a sample menu
    menu_data = {
        "dish": "ham sandwich",
        "price": "10",
        "calories": "100",
        "foodCategory": "sandwich",
    }

    menu_object = model.Menu(**menu_data)

    # Call the create function
    created_menu = controller.create(db_session, menu_object)

    # type: ignore is to tell pyright to ignore an error.
    # Assertions
    assert created_menu is not None
    assert created_menu.dish == "ham sandwich"  # type: ignore
    assert created_menu.price == "10"  # type: ignore
    assert created_menu.calories == "100"  # type: ignore
    assert created_menu.foodCategory == "sandwich"  # type: ignore

