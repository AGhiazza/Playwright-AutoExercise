# Playwright-AutoExercise

![CI Status](https://github.com/AGhiazza/Playwright-AutoExercise/actions/workflows/ci.yml/badge.svg)

## Description

QA Automation portfolio project — second project in the automation learning path. This project implements a complete UI and API test suite against [automationexercise.com](https://automationexercise.com), a public e-commerce practice site.

Built with Python and Playwright, applying professional automation patterns including Page Object Model, data-driven testing, session management with `storage_state`, API testing, CI/CD integration, and structured reporting with Allure.

---

## Technologies and Tools

- **Python 3.14** — Main language
- **Playwright 1.61.0** — Browser automation
- **pytest-playwright 0.8.0** — Playwright integration with pytest
- **pytest 9.1.1** — Testing framework
- **allure-pytest 2.16.0** — Allure report generation
- **Logging** — Execution logging system
- **GitHub Actions** — CI/CD pipeline
- **Claude Sonnet 4.6 (Anthropic)** — AI development assistance
- **Git / GitHub** — Version control

---

## Installation

### Prerequisites
- Python 3.10+
- Git
- [Allure CLI](https://allurereport.org/docs/install/) (for report generation)

### Steps

```bash
# 1. Clone the repository
git clone https://github.com/AGhiazza/Playwright-AutoExercise.git
cd Playwright-AutoExercise

# 2. Create and activate virtual environment
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # macOS/Linux

# 3. Install dependencies
pip install -r requirements.txt

# 4. Install Playwright browsers
playwright install
```

---

## Project Structure

```
Playwright-AutoExercise/
│
├── data/                        # Test data files
│   ├── navigation_data.json     # Categories, brands and search terms
│   └── user_data.json           # User credentials and registration data
│
├── pages/                       # Page Object Model classes
│   ├── base_page.py             # BasePage — shared elements and methods
│   ├── cart_page.py
│   ├── checkout_page.py
│   ├── contact_page.py
│   ├── home_page.py
│   ├── login_page.py
│   ├── payment_page.py
│   ├── product_detail_page.py
│   ├── products_page.py
│   └── register_page.py
│
├── reports/
│   ├── allure-results/          # Raw Allure output (generated, not tracked)
│   ├── logs/                    # Execution logs (generated, not tracked)
│   └── screenshots/             # Screenshots on failure (generated, not tracked)
│
├── tests_api/                   # API test suite
│   ├── test_auth.py             # AU: Login verification
│   ├── test_brands.py           # BR: Brands list
│   ├── test_products.py         # PL: Products list
│   ├── test_search.py           # SR: Product search
│   └── test_user.py             # US: User account lifecycle
│
├── tests_ui/                    # UI test suite
│   ├── test_cart.py             # CA: Cart operations
│   ├── test_checkout.py         # CH: Checkout flow
│   ├── test_contact.py          # CT: Contact form
│   ├── test_delete.py           # DE: Account deletion
│   ├── test_E2E.py              # E2E: End-to-end flows
│   ├── test_login.py            # LO: Login / Logout
│   ├── test_navigation.py       # NA: Category and brand navigation
│   ├── test_payment.py          # PY: Payment and invoice
│   ├── test_product_detail.py   # PD: Product detail and reviews
│   ├── test_products.py         # PR: Product search
│   ├── test_register.py         # RE: User registration
│   ├── test_smoke.py            # Smoke test
│   └── test_subscription.py     # SU: Newsletter subscription
│
├── utils/
│   ├── data_reader.py           # JSON file reader utility
│   └── logger.py                # Logger configuration
│
├── conftest.py                  # Shared fixtures and hooks
├── pytest.ini                   # pytest configuration
├── requirements.txt             # Python dependencies
└── testcaseslist.md             # Full test case documentation
```

---

## Patterns and Conventions

### Page Object Model (POM)
Every page has its own class inheriting from `BasePage`. Locators are defined as `@property` returning live Playwright locators, evaluated at call time rather than at instantiation.

```python
@property
def login_button(self):
    return self.page.locator("[data-qa='login-button']")
```

### Data-Driven Testing
Test data is stored in JSON files under `data/`. A `read_json()` utility in `utils/data_reader.py` handles file loading. Parametrized tests (categories, brands, login fields) read directly from these files.

### Session Management with `storage_state`
For tests that require an authenticated user without repeating the login flow, Playwright's `storage_state` is used to save and restore browser session cookies. Implemented in the `logged_in_page` fixture in `conftest.py`.

### API-Assisted Setup and Teardown
Tests that require a registered user use the `registered_user` fixture, which creates the user via API before the test and deletes it via API after — avoiding UI dependency for test setup.

### Conventional Commits
All commits follow the [Conventional Commits](https://www.conventionalcommits.org/) specification:
- `feat:` — new feature or test
- `fix:` — bug fix
- `refactor:` — code restructuring without behavior change
- `chore:` — maintenance tasks
- `test:` — test additions or changes

### Test IDs
Tests are identified with prefixes indicating their domain:

| Prefix | Domain |
|---|---|
| `LO` | Login / Logout |
| `RE` | Registration |
| `DE` | Account Deletion |
| `NA` | Navigation |
| `SU` | Subscription |
| `PD` | Product Detail |
| `PR` | Product Search |
| `CA` | Cart |
| `CH` | Checkout |
| `PY` | Payment |
| `CT` | Contact Us |
| `E2E` | End to End |
| `SR` | API Search |
| `AU` | API Auth |
| `BR` | API Brands |
| `PL` | API Products |
| `US` | API User |

---

## Test Cases

Full test case documentation — including descriptions, preconditions and expected results — is available in [`testcaseslist.md`](./testcaseslist.md).

**Suite summary:**
- **UI tests:** 42 active + 3 skipped (browser-native validations)
- **API tests:** 11
- **Total:** 56 collected

---

## Running the Tests

### Full suite
```bash
pytest
```

### UI tests only
```bash
pytest tests_ui/
```

### API tests only
```bash
pytest tests_api/
```

### By marker
```bash
pytest -m ui
pytest -m api
pytest -m e2e
pytest -m smoke
```

### With Allure report generation
```bash
pytest --alluredir=reports/allure-results
allure serve reports/allure-results
```

### Headed mode (visible browser)
```bash
pytest --headed
```

---

## Reports

### Allure Report
Allure results are generated automatically in `reports/allure-results/` on every run (configured in `pytest.ini`). To view the report:

```bash
allure serve reports/allure-results
```

> Note: `reports/allure-results/` is listed in `.gitignore` and is not tracked by Git.

### Logs
Execution logs are saved automatically to `reports/logs/` with a timestamped filename (`log_YYYY-MM-DD_HH-MM-SS.log`). Each log entry includes:
- Timestamp
- Log level (INFO / ERROR)
- Logger name
- Message

Test start and end are logged automatically via a `conftest.py` fixture. Failed tests are logged as ERROR via a pytest hook.

> Note: `reports/logs/` is listed in `.gitignore` and is not tracked by Git.

### Screenshots on Failure
Playwright is configured to capture screenshots automatically when a test fails. Screenshots are saved to `reports/screenshots/` (configured via `--screenshot=only-on-failure` in `pytest.ini`).

> Note: `reports/screenshots/` is listed in `.gitignore` and is not tracked by Git.

---

## CI/CD

This project uses **GitHub Actions** for continuous integration. The pipeline runs automatically on every push and pull request to `main`.

### What it does
1. Sets up Python 3.13 on Ubuntu
2. Installs all dependencies from `requirements.txt`
3. Installs Chromium browser via Playwright
4. Runs the full test suite (`pytest`)
5. Uploads Allure results as a downloadable artifact

The workflow file is located at `.github/workflows/ci.yml`.

---

## Notes

### Known Site Limitations

**Cart quantity field:** The quantity field in the cart appears interactive but does not respond to user input. This functionality is not covered in the test suite.

**Ad interference:** The site displays aggressive third-party ads that can occasionally interfere with UI interactions. The `context_no_ads` fixture in `conftest.py` blocks known ad domains for navigation tests. A `dismiss_ad()` method in `BasePage` handles ads that appear during interactions. Some residual flakiness may occur due to ads from unblocked domains.

### CI/CD Limitations

The CI pipeline runs the full test suite on every push, but may report failures due to limitations inherent to the practice site:

- **Third-party ads** interfere with UI interactions in headless mode on GitHub's runner network.
- **Session persistence** — the site's user accounts and sessions are shared and may be affected by other users or previous runs.
- **Network latency** — GitHub's runner network may cause timeouts on a site not designed for CI environments.

The first CI run (CI #1) completed successfully and serves as baseline evidence of suite stability. Local execution consistently achieves 100% pass rate on a clean run.

### API Defects Found

During API testing, the following discrepancies were identified between the documented behavior and the actual API responses. All HTTP responses return status 200 regardless of the operation result; the actual response code is included in the JSON body under `responseCode`.

| Test | Documented Response | Actual Response | Notes |
|---|---|---|---|
| `PL02` | HTTP 405 | HTTP 200, responseCode 200 | POST to products list not rejected |
| `BR02` | HTTP 405 | HTTP 200, responseCode 200 | PUT to brands list not rejected |
| `SR02` | HTTP 400 | HTTP 200, responseCode 400 | Missing parameter returns 200 with error in body |
| `AU02` | HTTP 400 | HTTP 200, responseCode 400 | Missing parameter returns 200 with error in body |
| `AU03` | HTTP 405 | HTTP 200, responseCode 405 | Wrong method returns 200 with error in body |
| `AU04` | HTTP 404 | HTTP 200, responseCode 404 | Invalid credentials returns 200 with error in body |

All API tests assert against the `responseCode` field in the response body, not the HTTP status code, to account for this behavior.

### `storage_state` Implementation
Playwright's `storage_state` is implemented in the `logged_in_page` fixture, demonstrating session persistence without repeated login flows. Due to the site's user management behavior (some tests create and delete users as part of the flow), this fixture is applied selectively to tests that use a stable, persistent user account.

### Skipped Tests
Three tests are marked with `@pytest.mark.skip` as they cover browser-native HTML5 validation (required field tooltips), which is not application logic and does not require automation:
- `LO02` — Login with empty fields
- `PY03` — Payment with empty card field
- `CT02` — Contact form with empty email
