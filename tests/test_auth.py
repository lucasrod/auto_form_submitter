from auth.login_handler import LoginHandler

def test_login():
    login_handler = LoginHandler(headless=True)
    page = login_handler.login()

    assert "/UserArea" in page.url, "No se redirigió correctamente al procedimiento de reserva consular después del login."

    login_handler.close()