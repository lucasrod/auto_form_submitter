from abc import ABC, abstractmethod

class AbstractScraper(ABC):
    @abstractmethod
    def login(self):
        """Authenticate to the website."""
        pass

    @abstractmethod
    def submit_form(self, payload: dict):
        """Submit the form with the given payload."""
        pass

    @abstractmethod
    def schedule_appointment(self):
        """Schedule an appointment if available."""
        pass