# Selenium Login Automation – SauceDemo

## 📌 Project Overview

This project automates the login flow for the [SauceDemo](https://www.saucedemo.com/) shopping site using **Selenium WebDriver** in Python.

Key highlights:
- Uses the **Page Object Model (POM)** for clean, reusable locators and actions.
- Implements tests using **pytest** (TDD) and **behave** (BDD).
- Demonstrates practical web UI automation workflows.

---

## ⚙️ Tech Stack

- Python
- Selenium WebDriver
- Pytest
- Behave (BDD)

---

## 📂 Project Structure

project_root/
├── pages/ # Page Object Model classes
├── tests_pytest/ # TDD tests using pytest
├── tests_behave/ # BDD tests using behave
├── drivers/ # WebDriver executables (optional)
├── requirements.txt # Python dependencies
└── README.md

---

## 🚀 How to Run

1️⃣ **Clone the repo**
```bash
git clone <YOUR_REPO_URL>
cd <repo_name>

---
## Create virtual environment & install dependencies

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt

---
## Run pytest tests

pytest tests_pytest/

## Run behave tests

behave tests_behave/


