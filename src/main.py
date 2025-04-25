import logging
import json
import time
from dotenv import load_dotenv
from auth.login_handler import LoginHandler
from forms.form_handler import FormHandler
from scheduler.appointment_scheduler import AppointmentScheduler


from utils.env_loader import load_environment

load_environment()

from auth.login_handler import LoginHandler

handler = LoginHandler()
handler.login()


load_dotenv()  # Ensure environment variables are loaded

# Configure logging
logging.basicConfig(
    filename='logs/app.log',
    level=logging.INFO,
    format='%(asctime)s %(levelname)s: %(message)s'
)

def load_payload_template():
    with open('data/form_payload_templates.json', 'r') as f:
        return json.load(f)


def main():
    logging.info("Starting auto_form_submitter process...")

    # 1. Authenticate
    login_handler = LoginHandler()
    driver = login_handler.login()

    # 2. Inspect available form structure
    form_handler = FormHandler(driver)
    form_handler.inspect_form()

    # 3. Load form payload template (adjust key based on form)
    payload_template = load_payload_template()
    payload = payload_template.get('default', {})

    # 4. Submit the form
    form_handler.submit_form(payload)

    # 5. Monitor and schedule appointment if available
    scheduler = AppointmentScheduler(driver)
    for attempt in range(10):  # Polling loop: adjust max attempts as needed
        if scheduler.check_availability():
            scheduler.schedule_appointment()
            break
        else:
            logging.info("No appointment available, retrying in 1 second...")
            time.sleep(1)

    logging.info("Process completed, closing browser.")
    driver.quit()


if __name__ == '__main__':
    main()