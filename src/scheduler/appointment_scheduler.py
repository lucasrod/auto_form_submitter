import logging
import time
from selenium.webdriver.common.by import By

class AppointmentScheduler:
    def __init__(self, driver):
        self.driver = driver

    def check_availability(self):
        logging.info("Checking for available appointment slots...")
        try:
            # Example: Look for an element with ID "available_slot"
            element = self.driver.find_element(By.ID, 'available_slot')
            if element.is_displayed():
                logging.info("Appointment slot available!")
                return True
        except Exception as e:
            logging.info("No appointment slots available at this time.")
        return False

    def schedule_appointment(self):
        logging.info("Attempting to schedule appointment...")
        if self.check_availability():
            self.driver.find_element(By.ID, 'available_slot').click()
            logging.info("Appointment scheduled successfully!")
        else:
            logging.warning("Failed to schedule appointment: No slots available.")