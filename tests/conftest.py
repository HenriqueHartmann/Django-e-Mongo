import pytest
from rest_framework_mongoengine.test import APIClient


@pytest.fixture()
def api_client():
    return APIClient()
