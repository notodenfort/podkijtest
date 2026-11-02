import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from api import register_endpoint
from tests.test_users import FakeMailer
from users import InMemoryUserRepository, UserService


def test_register_endpoint_success():
    repository = InMemoryUserRepository()
    mailer = FakeMailer()
    service = UserService(repository, mailer)

    status_code, body = register_endpoint(
        service,
        {"email": "anna@example.com", "password": "secret123"}
    )

    assert status_code == 201
    assert body == {"email": "anna@example.com"}
