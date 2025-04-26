# 🚀 Auto Form Submitter

## 📌 Overview
Auto Form Submitter is a Python-based automation tool that:
- Authenticates to a website using credentials.
- Monitors, fills, and submits a form as soon as it becomes available.
- Supports scheduling appointments dynamically.
- Uses **Selenium** and **Playwright** for reliable browser automation.

## 🛠️ Features
✔️ Automatic login and session handling  
✔️ Form payload customization (JSON-based templates)  
✔️ Appointment scheduler with retry logic  
✔️ Logging and exception handling for debugging  
✔️ Modular and extensible architecture  

## 📦 Installation

### 1️⃣ Clone the Repository
```
git clone https://github.com/YOUR_USERNAME/auto-form-submitter.git
cd auto-form-submitter
```

### 2️⃣ Set Up a Virtual Environment (Using Conda)
```
conda create --name auto_form_submitter python=3.11
conda activate auto_form_submitter
```

### 3️⃣ Install Dependencies
```
pip install -r requirements.txt
playwright install  # Install required browsers
```

## ⚙️ Configuration
### Setting Up Environment Variables
All environment variables live in the `config/` directory. Create one of the following files:

- `config/.env` (fallback defaults):
  ```ini
  ENVIRONMENT=TESTING
  USERNAME=testuser@gmail.com
  PASSWORD=testpass
  GMAIL_USER=testuser@gmail.com
  GMAIL_PASS=testpass
  ```
- `config/.env.testing` (explicit testing mode):
  ```ini
  ENVIRONMENT=TESTING
  USERNAME=<your_test_username>
  PASSWORD=<your_test_password>
  GMAIL_USER=<your_gmail_user>
  GMAIL_PASS=<your_gmail_pass>
  ```
- `config/.env.prod` (production mode – do NOT commit real secrets):
  ```ini
  ENVIRONMENT=PROD
  USERNAME=<your_prod_username>
  PASSWORD=<your_prod_password>
  GMAIL_USER=<your_gmail_user>
  GMAIL_PASS=<your_gmail_pass>
  ```

## 🚀 Usage
Run the main script to start monitoring and submitting the form:
```
python src/main.py
```

## 🔄 Execution Flow
When you run `python src/main.py`, the following steps are executed in order:

1. **Load environment**: `utils/env_loader.load_environment()` reads `config/.env*` and sets all required variables.
2. **Initialize logging**: logs are written to `logs/app.log` with timestamp and level.
3. **Authenticate**: `LoginHandler` launches a headless browser, navigates to the login page, fills credentials, and waits for `/UserArea`.
4. **Inspect & submit form**: `FormHandler` analyses the booking form, loads a JSON payload template from `data/form_payload_templates.json`, and submits it.
5. **Poll for availability**: `AppointmentScheduler` checks up to 10 times for available slots (with 1 s interval), and schedules when found.
6. **Cleanup**: the browser session is closed via `login_handler.close()`.

## 🧪 Running Tests
To execute the full test suite in **TESTING** mode, follow these steps:

```bash
# 1. Create and activate the Conda environment
conda env create -f environment.yml
conda activate auto_form_submitter

# 2. Install dependencies and browsers
pip install -r requirements.txt
playwright install  # download required browser binaries

# 3. Run tests under the testing environment
export ENVIRONMENT=TESTING
pytest -q
```

## 📜 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
