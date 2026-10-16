# Saucedemo Test Log

A test log is the scoreboard of every check that was run, pass or fail. A bug report is written only when a check fails, and the Bug ID column points to it.

| Test ID | What was checked | Result | Bug ID | Jira ID |
|---|---|---|---|---|
| LG-001 | Login as `problem_user` with a valid password | Pass | None | None |
| LG-002 | Login as `standard_user` with a valid password | Re-run pending | None | None |
| LG-003 | Login rejected when the username is an email address | Pass | None | None |
| LG-004 | Login rejected when the username is wrong | Pass | None | None |
| LG-005 | Login rejected when the password is wrong | Pass | None | None |
| LG-006 | Login rejected when both fields are empty | Pass | None | None |
| TC-CART-001 | Add each product to the cart as `problem_user` | Fail | BUG-003 | KAN-4 |
| TC-PROD-001 | Product images match product names (`problem_user`) | Fail | BUG-004 | KAN-5 |
| TC-CHK-001 | Fill in name and postal code on the checkout information page (`problem_user`) | Fail | BUG-005 | KAN-6 |

The login cases (LG-001 to LG-006) are written out in full in `03-saucedemo-login-test-cases.md`. The three failing checks are described in `05-saucedemo-bug-reports.md`.

*Earlier drafts of this log called the first two checks TC-LOGIN-001 and TC-LOGIN-002. They are now LG-001 and LG-002 so the IDs match the test case file.*
