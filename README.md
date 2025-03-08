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
Create a `.env` file inside the `config/` directory and add:
```
USERNAME=your_username
PASSWORD=your_password
LOGIN_URL=https://example.com/login
```

## 🚀 Usage
Run the main script to start monitoring and submitting the form:
```
python src/main.py
```

## 🧪 Running Tests
To run unit tests:
```
pytest tests/
```

## 📜 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
