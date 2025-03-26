import logging
import os
from dotenv import load_dotenv
from utils.abstract_scraper import AbstractScraper
from utils.browser import Browser
from playwright.sync_api import expect

dotenv_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../config/.env"))
load_dotenv(dotenv_path=dotenv_path)

class LoginHandler(AbstractScraper):
    def __init__(self, headless=True):
        self.browser = Browser(headless)
        self.username = os.getenv('USERNAME')
        self.password = os.getenv('PASSWORD')
        self.login_url = os.getenv('LOGIN_URL')

    def login(self):
        logging.info("Navigating to login page...")
        page = self.browser.new_page()
        page.goto(self.login_url)

        page.fill("#login-email", self.username)
        page.fill("#login-password", self.password)

        logging.info("Submitting credentials...")
        page.click('button[type="submit"]')

        # Esperar hasta la redirección al Prenotazione Consolare Procedura
        page.wait_for_url("**/UserArea", timeout=200000)

        logging.info("Login successful.")
        return page

    def submit_form(self, payload: dict):
        raise NotImplementedError("LoginHandler does not implement form submission.")

    def schedule_appointment(self):
        raise NotImplementedError("LoginHandler does not implement appointment scheduling.")

    def close(self):
        self.browser.close()