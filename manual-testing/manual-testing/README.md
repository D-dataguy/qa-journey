# Manual Testing Portfolio

My manual testing work from my QA learning path: test design, test cases, bug reports, API checks and the notes behind them.
The automated (Python, pytest, requests) versions of the API tests are in `test_api.py` at the top level of this repo.

## Contents

| File | What it covers |
|---|---|
| [01-signup-form-test-cases.md](01-signup-form-test-cases.md) | Requirement analysis and test cases for a signup form (password length rule) |
| [02-boundary-value-tables.md](02-boundary-value-tables.md) | Equivalence partitioning and boundary value analysis: password, age, phone number, username |
| [03-saucedemo-login-test-cases.md](03-saucedemo-login-test-cases.md) | Test scenarios and test cases for the Saucedemo login page |
| [04-saucedemo-test-log.md](04-saucedemo-test-log.md) | Test execution log (pass/fail) linked to bug IDs and Jira tickets |
| [05-saucedemo-bug-reports.md](05-saucedemo-bug-reports.md) | Three bug reports found with the `problem_user` account |
| [06-api-test-cases.md](06-api-test-cases.md) | API test cases (Postman) against JSONPlaceholder |
| [07-notes-and-cheatsheets.md](07-notes-and-cheatsheets.md) | Notes: testing types, bug life cycle, Agile/Scrum, API basics, checklists |

## Tools used

Google Chrome, Jira (free plan), Postman, Python with pytest and requests, Git and GitHub.

## Practice targets (public sites made for practice)

- Saucedemo: https://www.saucedemo.com
- JSONPlaceholder: https://jsonplaceholder.typicode.com

---

## BEFORE YOU PUBLISH (delete this section when done)

These items need your own screen, so I could not fill them in for you:

- [ ] Replace every `[Chrome version]` with your real version (three-dot menu, Help, About Google Chrome).
- [ ] **LG-002** (file 03): re-run it with the username `standard_user` (copy the name from the "Accepted usernames" box on the Saucedemo login page) and confirm the result.
- [ ] **LG-003 to LG-006** (file 03): copy the error message from the screen character for character into each Actual result. The site's messages may start with a prefix such as "Epic sadface:".
- [ ] **BUG-003, BUG-004, BUG-005** (file 05): reproduce each one once more and confirm the steps, the product names, the values you typed, and the reproducibility count. Your observation always wins over my wording.
- [ ] Add your screenshots and recordings (see the Evidence line in each bug) and fix the links.
- [ ] Check the Jira IDs in files 04 and 05 against your board (they were KAN-4, KAN-5 and KAN-6 when I last saw it).
- [ ] The phone numbers in file 02 are made-up examples. Do not replace them with a real number, because this repo is public.
- [ ] Read each file once, aloud, for typos and for data that does not match its steps.
