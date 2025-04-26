import pytest
from selenium.webdriver.common.by import By
from scheduler.appointment_scheduler import AppointmentScheduler


class DummyElement:
    def __init__(self, displayed=True):
        self._displayed = displayed
        self.clicked = False

    def is_displayed(self):
        return self._displayed

    def click(self):
        self.clicked = True


class DriverAvailable:
    def __init__(self):
        self.clicked = False

    def find_element(self, by, selector):
        assert by == By.ID and selector == 'available_slot'
        el = DummyElement(displayed=True)
        # wrap click to record
        def click():
            self.clicked = True
            el.clicked = True
        el.click = click
        return el


class DriverHidden:
    def find_element(self, by, selector):
        assert by == By.ID and selector == 'available_slot'
        return DummyElement(displayed=False)


class DriverUnavailable:
    def find_element(self, by, selector):
        raise Exception("not available")


def test_check_availability_true():
    scheduler = AppointmentScheduler(DriverAvailable())
    assert scheduler.check_availability() is True


def test_check_availability_false_when_hidden():
    scheduler = AppointmentScheduler(DriverHidden())
    assert scheduler.check_availability() is False


def test_check_availability_false_on_exception():
    scheduler = AppointmentScheduler(DriverUnavailable())
    assert scheduler.check_availability() is False


def test_schedule_appointment_clicks_when_available():
    driver = DriverAvailable()
    scheduler = AppointmentScheduler(driver)
    # Force availability
    scheduler.schedule_appointment()
    assert driver.clicked is True