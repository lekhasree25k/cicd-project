# CI/CD Pipeline for Python Application

![CI Pipeline](https://github.com/YOUR_USERNAME/YOUR_REPO_NAME/actions/workflows/ci.yml/badge.svg)

## Project Overview

A DevOps mini project demonstrating a complete CI/CD pipeline for a Python application using **Git**, **GitHub**, and **GitHub Actions**.

Every time code is pushed to this repository, the pipeline automatically:
1. Sets up a clean Ubuntu environment
2. Installs Python and all dependencies
3. Runs all unit tests using `pytest`
4. Reports pass/fail status

---

## Project Structure

```
cicd-project/
├── app.py                        # Python application (calculator functions)
├── test_app.py                   # Unit tests using pytest
├── requirements.txt              # Project dependencies
├── README.md                     # Project documentation
└── .github/
    └── workflows/
        └── ci.yml                # GitHub Actions pipeline definition
```

---

## How to Run Locally

```bash
# 1. Clone the repository
git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
cd YOUR_REPO_NAME

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the application
python app.py

# 4. Run the tests
pytest test_app.py -v

# 5. Run tests with coverage
pytest test_app.py -v --cov=app --cov-report=term-missing
```

---

## CI/CD Pipeline

The pipeline is defined in `.github/workflows/ci.yml` and runs on every `push` and `pull_request` to `main`.

### Pipeline Steps

| Step | Action |
|------|--------|
| Checkout | Downloads the latest code onto the runner |
| Setup Python | Installs Python 3.11 on the Ubuntu runner |
| Install dependencies | Runs `pip install -r requirements.txt` |
| Run tests | Executes `pytest` — fails the pipeline if any test fails |
| Coverage report | Shows which lines of code are covered by tests |

---

## Technologies Used

- **Python 3.11** — Application language
- **pytest** — Testing framework
- **Git** — Version control
- **GitHub** — Remote repository hosting
- **GitHub Actions** — CI/CD automation platform

---

## Author

Lekha Sree  

