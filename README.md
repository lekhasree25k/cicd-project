# CI/CD Pipeline for Python Application
![CI](https://github.com/lekhasree25k/cicd-project/actions/workflows/ci.yml/badge.svg)

## Project Overview

A DevOps mini project demonstrating a complete CI/CD pipeline for a Python application using **Git**, **GitHub**, **GitHub Actions** and **Docker**, tested on an **AWS EC2** server.

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
├── Dockerfile                    # Docker image recipe
├── README.md                     # Project documentation
└── .github/
    └── workflows/
        └── ci.yml                # GitHub Actions pipeline definition
```

---

## How to Run Locally

```bash
git clone https://github.com/lekhasree25k/cicd-project.git
cd cicd-project
pip install -r requirements.txt
python app.py
pytest test_app.py -v
```

---

## Run with Docker

```bash
docker build -t calc-app .
docker run --rm calc-app
docker run --rm calc-app pytest -v
```

All 23 tests pass inside the container.

---

## CI/CD Pipeline

The pipeline is defined in `.github/workflows/ci.yml` and runs on every `push` and `pull_request` to `main`.

| Step | Action |
|------|--------|
| Checkout | Downloads the latest code onto the runner |
| Setup Python | Installs Python 3.11 on the Ubuntu runner |
| Install dependencies | Runs `pip install -r requirements.txt` |
| Run tests | Executes `pytest` and fails the pipeline if any test fails |
| Coverage report | Shows which lines of code are covered by tests |

---

## Deployment

The Docker image was built and run on an AWS EC2 (Ubuntu) server, accessed over SSH.

---

## Technologies Used

- **Python 3.11**, **pytest**
- **Docker**
- **Git**, **GitHub**, **GitHub Actions**
- **AWS EC2**, **Linux (Ubuntu)**

---

## Author

Lekha Sree
