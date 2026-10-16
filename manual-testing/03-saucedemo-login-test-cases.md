# Saucedemo Login Page: Scenarios and Test Cases

- **Application:** https://www.saucedemo.com (a public practice shop)
- **Environment:** Chrome [Chrome version], Windows 11
- Valid usernames are the ones in the "Accepted usernames" box on the login page, for example `standard_user` and `problem_user`. The shared password is shown on the same page.

## Test scenarios

1. Verify that entering a valid username and password grants access to the website.
2. Verify that special characters like `@` or `%` do not disrupt the site. *(Requirement gap: allowed characters are not defined.)*
3. Verify the behaviour when the username contains a space. *(Requirement gap.)*
4. Verify that an incorrect username or password cannot access the website.
5. Verify that the username and password are case sensitive.
6. Verify that each valid account lands on the products page after login.

Scenarios 1 and 4 are expanded into test cases below. Scenarios 2, 3, 5 and 6 are not yet written (see the end of this file).

> **Note on the "Actual" lines:** wording was recorded while testing. Before publishing, copy each message from the screen character for character.

---

## Scenario 1: valid login

### LG-001: Login is accepted with a valid username and password
- **Label:** Positive
- **Preconditions:** the login page is open at https://www.saucedemo.com
- **Test data:** username `problem_user`, password `secret_sauce`
- **Steps:**
  1. Type the username in the Username field.
  2. Type the password in the Password field.
  3. Click Login.
- **Expected:** login succeeds and the products page opens.
- **Actual:** the account logged in and the products page opened.
- **Verdict:** Pass

### LG-002: Login is accepted with a second valid account
- **Label:** Positive
- **Preconditions:** the login page is open at https://www.saucedemo.com
- **Test data:** username `standard_user`, password `secret_sauce`
- **Steps:**
  1. Type the username in the Username field.
  2. Type the password in the Password field.
  3. Click Login.
- **Expected:** login succeeds and the products page opens.
- **Actual:** *(re-run with `standard_user` and record what happened; the first draft of this case used a username that is not on the accepted list)*
- **Verdict:** *(fill in after the re-run)*

---

## Scenario 4: incorrect credentials are rejected

### LG-003: Login is rejected when the username is an email address
- **Label:** Negative
- **Preconditions:** the login page is open at https://www.saucedemo.com
- **Test data:** username `problem_user@hg.com`, password `secret_sauce`
- **Steps:**
  1. Type the username in the Username field.
  2. Type the password in the Password field.
  3. Click Login.
- **Expected:** login is rejected, because the email does not match any user.
- **Requirement gap:** the error message wording is not defined.
- **Actual:** "username and password do not match any user in this service" *(copy the exact text from the screen)*
- **Verdict:** Pass

### LG-004: Login is rejected when the username is wrong
- **Label:** Negative
- **Preconditions:** the login page is open at https://www.saucedemo.com
- **Test data:** username `solution_getter`, password `secret_sauce`
- **Steps:**
  1. Type the username in the Username field.
  2. Type the password in the Password field.
  3. Click Login.
- **Expected:** login is rejected, because the username does not match any user.
- **Requirement gap:** the error message wording is not defined.
- **Actual:** "username and password do not match any user in this service" *(copy the exact text from the screen)*
- **Verdict:** Pass

### LG-005: Login is rejected when the password is wrong
- **Label:** Negative
- **Preconditions:** the login page is open at https://www.saucedemo.com
- **Test data:** username `problem_user`, password `secret_sauce@#`
- **Steps:**
  1. Type the username in the Username field.
  2. Type the password in the Password field.
  3. Click Login.
- **Expected:** login is rejected, because the password does not match.
- **Requirement gap:** the error message wording is not defined.
- **Actual:** "username and password do not match any user in this service" *(copy the exact text from the screen)*
- **Verdict:** Pass

### LG-006: Login is rejected when both fields are left empty
- **Label:** Negative
- **Preconditions:** the login page is open at https://www.saucedemo.com
- **Test data:** none
- **Steps:**
  1. Leave the Username field empty.
  2. Leave the Password field empty.
  3. Click Login.
- **Expected:** login is rejected, because both fields are empty.
- **Requirement gap:** the error message wording is not defined.
- **Actual:** "Username is required" *(copy the exact text from the screen)*
- **Verdict:** Pass

---

## Not written yet

- Scenario 2: special characters in the username.
- Scenario 3: a space in the username.
- Scenario 5: case sensitivity (for example `STANDARD_USER`).
- Scenario 6: every valid account lands on the products page.
- The locked-out account listed on the login page, and logging out.
