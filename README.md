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
