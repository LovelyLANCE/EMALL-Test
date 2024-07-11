import pytest
import os
import sys
from emall.app import create_app
from emall.database import Database

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client
