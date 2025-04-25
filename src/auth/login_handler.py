import logging
import os
from utils.abstract_scraper import AbstractScraper
from utils.browser import Browser

class LoginHandler(AbstractScraper):
    def __init__(self, headless=True):
        self.browser = Browser(headless)
        self.username = os.getenv('USERNAME')
        self.password = os.getenv('PASSWORD')
        self.login_url = 'https://prenotami.esteri.it/'

    def login(self):
        logging.info("Navigating to login page...")
        page = self.browser.new_page()
        page.goto(self.login_url)

        logging.info("Filling credentials...")
        page.fill("#login-email", self.username)
        page.fill("#login-password", self.password)

        logging.info("Submitting credentials...")
        page.click('button[type="submit"]')

        # Wait for redirect to UserArea
        page.wait_for_url("**/UserArea", timeout=200000)

        logging.info("Login successful.")
        return page

    def submit_form(self, payload: dict):
        raise NotImplementedError("LoginHandler does not implement form submission.")

    def schedule_appointment(self):
        raise NotImplementedError("LoginHandler does not implement appointment scheduling.")

    def close(self):
        self.browser.close()