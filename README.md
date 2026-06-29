# Playwright API Automation with Python

A beginner-friendly Playwright automation project built using **Python**, covering both **UI Automation** and **API Testing** with **Pytest**. This repository demonstrates browser automation, REST API validation, and HTML report generation.

## Features

- UI Automation using Playwright
- API Testing using Requests
- Pytest Test Cases
- Assertions and Validations
- OrangeHRM Login Automation
- JSONPlaceholder API Testing
- HTML Test Report Generation
- Simple and Clean Python Code

## Project Structure

```
PLAYWRIGHT_API/
│
├── playwright_practice.py      # Playwright UI automation
├── test_login.py               # Login test
├── test_api.py                 # API test cases
├── main.py                     # API CRUD examples
├── report.html                 # Pytest HTML Report
├── index.html                  # HTML Report
├── requirements.txt
└── README.md
```

## Technologies Used

- Python 3
- Playwright
- Pytest
- Requests
- pytest-html

## Installation

Clone the repository

```bash
git clone https://github.com/Vansh13code/PLAYWRIGHT_API.git
```

Move to the project directory

```bash
cd PLAYWRIGHT_API
```

Install dependencies

```bash
pip install -r requirements.txt
```

Install Playwright browsers

```bash
playwright install
```

## Running UI Tests

```bash
pytest test_login.py
```

or

```bash
python playwright_practice.py
```

## Running API Tests

```bash
pytest test_api.py
```

## Generate HTML Report

```bash
pytest --html=report.html
```

or

```bash
pytest --html=index.html
```

## UI Automation

The project automates the OrangeHRM Demo application and demonstrates:

- Browser Launch
- Browser Context
- Page Navigation
- Login
- Element Locators
- Click Actions
- Hover
- Keyboard Actions
- Mouse Actions
- Screenshots
- Cookies
- Local Storage
- Session Storage

## API Testing

The project uses JSONPlaceholder for API automation.

Covered HTTP Methods:

- GET
- POST
- PUT
- PATCH
- DELETE

Validation Includes:

- Status Code Validation
- JSON Response Validation
- Assertions
- Response Data Verification

## Test Websites

### OrangeHRM Demo

https://opensource-demo.orangehrmlive.com/

### JSONPlaceholder API

https://jsonplaceholder.typicode.com/


## Author

**Vansh Batra**

---

If you found this project helpful, consider giving it a ⭐ on GitHub.
