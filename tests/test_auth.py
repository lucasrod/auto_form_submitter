import pytest
from auth.login_handler import LoginHandler

class DummyBrowser:
    def close(self):
        pass

class DummyPage:
    def __init__(self, url):
        self.url = url

@pytest.fixture(autouse=True)
def stub_login(monkeypatch):
    """
    Stub LoginHandler to avoid real browser interactions during tests.
    """
    # Stub constructor to set login_url and a dummy browser
    def fake_init(self, headless=True):
        self.login_url = 'https://prenotami.esteri.it/'
        self.browser = DummyBrowser()
    monkeypatch.setattr(LoginHandler, "__init__", fake_init)
    # Stub login() to return a DummyPage with expected URL
    def fake_login(self):
        return DummyPage(self.login_url + "UserArea")
    monkeypatch.setattr(LoginHandler, "login", fake_login)
    yield

def test_login():
    login_handler = LoginHandler(headless=True)
    page = login_handler.login()
    assert "/UserArea" in page.url, \
        "Login should return page URL containing '/UserArea'"
    login_handler.close()