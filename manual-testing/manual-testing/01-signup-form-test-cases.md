# Signup Form: Requirement Analysis and Test Cases

**Status:** designed from a written requirement. There was no live signup form, so these cases have not been executed.

## Requirement

> The user enters a username, an email and a password. The password must be between 8 and 20 characters. On success, the user sees a welcome message.

## Requirement gaps (questions for the product owner)

The requirement does not say:

1. Which characters a password may or must contain (letters, numbers, symbols).
2. Whether username and email are both required to sign up, and which one is used to log in.
3. How strict email validation is (for example, is `user+test@mail.com` valid?).
4. Whether usernames and emails must be unique.
5. What happens on failure: whether an error message appears, what it says and where.

Valid email formats are decided by structure (something, `@`, a domain), not by provider. A form should not accept only Gmail or only Yahoo.

## Test cases

Each case uses its own username and email, so the cases can run in any order without affecting each other.

### TC-SU-001: Password with exactly 8 characters is accepted
- **Label:** Positive
- **Preconditions:** the signup page is open, and the username and email below are not already registered.
- **Test data:** username `tester01`, email `tester01@mail.com`, password `Abcd1234` (8 characters)
- **Steps:**
  1. Enter `tester01` in the username field.
  2. Enter `tester01@mail.com` in the email field.
  3. Enter `Abcd1234` in the password field.
  4. Click Sign up.
- **Expected result:** the account is created and the welcome message is shown.

### TC-SU-002: Password with 7 characters is rejected
- **Label:** Negative
- **Preconditions:** the signup page is open, and the username and email below are not already registered.
- **Test data:** username `tester02`, email `tester02@mail.com`, password `Abcd134` (7 characters)
- **Steps:**
  1. Enter `tester02` in the username field.
  2. Enter `tester02@mail.com` in the email field.
  3. Enter `Abcd134` in the password field.
  4. Click Sign up.
- **Expected result:** the account is not created and an error message is shown.
- **Requirement gap:** the requirement does not define the error message text or where it appears. The expected result is assumed. Clarify with the product owner or BA before execution.

### TC-SU-003: Password with 9 characters is accepted
- **Label:** Positive
- **Preconditions:** the signup page is open, and the username and email below are not already registered.
- **Test data:** username `tester03`, email `tester03@mail.com`, password `Abcd1234@` (9 characters)
- **Steps:**
  1. Enter `tester03` in the username field.
  2. Enter `tester03@mail.com` in the email field.
  3. Enter `Abcd1234@` in the password field.
  4. Click Sign up.
- **Expected result:** the account is created and the welcome message is shown.

### TC-SU-004: Password with exactly 20 characters is accepted
- **Label:** Positive
- **Preconditions:** the signup page is open, and the username and email below are not already registered.
- **Test data:** username `tester04`, email `tester04@mail.com`, password `Abcd1234@efghijtfsh$` (20 characters)
- **Steps:**
  1. Enter `tester04` in the username field.
  2. Enter `tester04@mail.com` in the email field.
  3. Enter `Abcd1234@efghijtfsh$` in the password field.
  4. Click Sign up.
- **Expected result:** the account is created and the welcome message is shown.

### TC-SU-005: Password with 21 characters is rejected
- **Label:** Negative
- **Preconditions:** the signup page is open, and the username and email below are not already registered.
- **Test data:** username `tester05`, email `tester05@mail.com`, password `Abcd1234@efghijtfsh$x` (21 characters)
- **Steps:**
  1. Enter `tester05` in the username field.
  2. Enter `tester05@mail.com` in the email field.
  3. Enter `Abcd1234@efghijtfsh$x` in the password field.
  4. Click Sign up.
- **Expected result:** the account is not created and an error message is shown.
- **Requirement gap:** the requirement does not define the error message text or where it appears. The expected result is assumed. Clarify with the product owner or BA before execution.

## Not written yet

- The 19-character boundary value (`Abcd1234@efghijtfs$`, 19 characters).
- A normal mid-range value (for example 12 characters).
- Empty password, spaces inside the password, and a duplicate signup.
