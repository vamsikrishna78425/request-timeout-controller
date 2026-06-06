# Request Timeout Controller

**Task 2 – Reliability Module**

- **Intern:** Vamsi Krishna Darla
- **Supervisor:** Vasudha Tayade
- **Captain:** Ayesha Faquih
- **Deadline:** 07/06/2026

---

## Overview

The Request Timeout Controller prevents application requests from running indefinitely and consuming excessive system resources. It introduces configurable timeout management, automatic request cancellation, middleware-based monitoring, and rollback handling for partially completed operations.

---

## Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Main programming language |
| FastAPI | API development framework |
| AsyncIO | Asynchronous request management |
| Uvicorn | ASGI server |
| Pytest | Testing framework |

---

## Project Structure

```

request-timeout-controller/
│
├── src/
│   ├── main.py
│   ├── timeout_manager.py
│   ├── middleware.py
│   └── __init__.py
│
├── tests/
│   └── test_timeout.py
│
├── requirements.txt
└── README.md
```

---

## Installation

```bash
pip install -r requirements.txt
```

---

## Run the App

```bash
uvicorn src.main:app --reload
```

---

## Run Tests

```bash
pytest tests/ -v
```

---

## Test Cases

| Test | Input | Expected | Result |
|------|-------|----------|--------|
| TC-1 | Delay=2s, Timeout=5s | Success | ✅ Passed |
| TC-2 | Delay=10s, Timeout=5s | Timeout | ✅ Passed |
| TC-3 | Concurrent requests | Timeout enforced | ✅ Passed |
| TC-4 | Partial execution | Rollback triggered | ✅ Passed |
