import pytest
from selenium.webdriver.common.by import By
from forms.form_handler import FormHandler


class DummyElement:
    def __init__(self, name=None):
        self.name = name
        self.cleared = False
        self.sent = []
        self.clicked = False

    def clear(self):
        self.cleared = True

    def send_keys(self, value):
        self.sent.append(value)

    def click(self):
        self.clicked = True


class DummyDriver:
    """
    Dummy driver for testing FormHandler.
    """
    def __init__(self):
        self.calls = []

    def find_elements(self, by, selector):
        assert by == By.TAG_NAME and selector == 'input'
        # Return a list of dummy elements (not used for submit)
        return [DummyElement(name=f'input{i}') for i in range(3)]

    def find_element(self, by, selector):
        if by == By.NAME:
            el = DummyElement(name=selector)
            # override methods to record calls
            orig_clear = el.clear
            def clear():
                self.calls.append(('clear', selector))
                orig_clear()
            el.clear = clear
            def send_keys(value):
                self.calls.append(('send_keys', selector, value))
                el.sent.append(value)
            el.send_keys = send_keys
            return el
        if by == By.ID and selector == 'form_submit':
            el = DummyElement(name=selector)
            def click():
                self.calls.append(('click', selector))
                el.clicked = True
            el.click = click
            return el
        raise ValueError(f"Unexpected find_element arguments: {by}, {selector}")


def test_inspect_form_returns_elements():
    driver = DummyDriver()
    handler = FormHandler(driver)
    elements = handler.inspect_form()
    assert isinstance(elements, list)
    assert all(isinstance(e, DummyElement) for e in elements)
    assert len(elements) == 3


def test_submit_form_clears_sends_and_clicks():
    payload = {'first_name': 'John', 'last_name': 'Doe'}
    driver = DummyDriver()
    handler = FormHandler(driver)
    handler.submit_form(payload)
    # Check that clear and send_keys were called for each field
    expected_calls = []
    for field, value in payload.items():
        expected_calls.append(('clear', field))
        expected_calls.append(('send_keys', field, value))
    # Finally, the form_submit button is clicked
    expected_calls.append(('click', 'form_submit'))
    assert driver.calls == expected_calls