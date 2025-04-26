import logging
import json
import time

from utils.env_loader import load_environment
from auth.login_handler import LoginHandler
from forms.form_handler import FormHandler
from scheduler.appointment_scheduler import AppointmentScheduler

def load_payload_template():
    """
    Load the JSON payload templates from disk.
    Returns a dict of named templates.
    """
    with open('data/form_payload_templates.json', 'r') as f:
        return json.load(f)


def main():
    """
    Main entry point: load environment, perform login, fill and submit form,
    and monitor for available appointments.
    """
    # 1. Load environment variables
    load_environment()

    # 2. Configure logging
    logging.basicConfig(
        filename='logs/app.log',
        level=logging.INFO,
        format='%(asctime)s %(levelname)s: %(message)s'
    )
    logging.info("Starting auto_form_submitter process...")

    # 3. Authenticate and obtain a browser page
    login_handler = LoginHandler()
    page = login_handler.login()

    # 4. Inspect form structure
    form_handler = FormHandler(page)
    form_handler.inspect_form()

    # 5. Load payload template and submit form
    payload_template = load_payload_template()
    payload = payload_template.get('default', {})
    form_handler.submit_form(payload)

    # 6. Monitor availability and schedule appointment
    scheduler = AppointmentScheduler(page)
    for attempt in range(10):  # Polling loop: adjust max attempts as needed
        if scheduler.check_availability():
            scheduler.schedule_appointment()
            break
        logging.info("No appointment available, retrying in 1 second...")
        time.sleep(1)

    # 7. Cleanup
    logging.info("Process completed, closing browser.")
    login_handler.close()


if __name__ == '__main__':
    main()