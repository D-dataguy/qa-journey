# API Test Cases: JSONPlaceholder

- **API:** https://jsonplaceholder.typicode.com (a free fake API for practice)
- **Tool:** Postman. Cases TC-API-001 to TC-API-003 are also automated in `test_api.py` (Python, pytest, requests).
- JSONPlaceholder pretends to save data but does not keep it, so a GET after a POST will not return the new item.

## What an API test checks

| Check | Example |
|---|---|
| Status code | 200, 201, 404 |
| Response body | the right fields, values and data types |
| Response time | within an agreed limit (Postman shows it) |
| Headers | the content type is JSON |
| Negative cases | bad input fails cleanly |

---

### TC-API-001: Get an existing user returns the correct details
- **Label:** Positive
- **Preconditions:** none (the API is public)
- **Test data:** user ID `1`
- **Steps:**
  1. Create a `GET` request to `https://jsonplaceholder.typicode.com/users/1`.
  2. Click Send.
- **Expected:** status `200 OK`. The body contains `"name": "Leanne Graham"` and `"email": "Sincere@april.biz"`.
- **Actual:** status `200 OK`, with that name and email.
- **Verdict:** Pass

### TC-API-002: Get a user that does not exist
- **Label:** Negative
- **Preconditions:** none
- **Test data:** user ID `9999`
- **Steps:**
  1. Create a `GET` request to `https://jsonplaceholder.typicode.com/users/9999`.
  2. Click Send.
- **Expected:** status `404 Not Found`, and the body is `{}`.
- **Actual:** status `404 Not Found`, body `{}`.
- **Verdict:** Pass

### TC-API-003: Create a post with valid data returns 201 Created
- **Label:** Positive
- **Preconditions:** none
- **Test data:**
  ```json
  {
    "title": "My first API test",
    "body": "Testing with Postman",
    "userId": 1
  }
  ```
- **Steps:**
  1. Create a `POST` request to `https://jsonplaceholder.typicode.com/posts`.
  2. Open the Body tab, choose raw and JSON, and paste the test data above.
  3. Click Send.
- **Expected:** status `201 Created`. The body contains the same `title`, `body` and `userId` as sent, and an `id` is present. (Check that an `id` exists, not that it equals a fixed number: a real API gives a different one each time.)
- **Actual:** status `201 Created`. The body returned `title`, `body`, `userId` and `"id": 101`.
- **Verdict:** Pass

### TC-API-004: Create a post without a title
- **Label:** Negative
- **Preconditions:** none
- **Test data:**
  ```json
  {
    "body": "Testing with Postman",
    "userId": 1
  }
  ```
- **Steps:**
  1. Create a `POST` request to `https://jsonplaceholder.typicode.com/posts`.
  2. Open the Body tab, choose raw and JSON, and paste the test data above.
  3. Click Send.
- **Expected:** the request is rejected with a `4xx` status (for example `400 Bad Request`), and no post is created.
- **Requirement gap:** the specification does not say whether `title` is required.
- **Actual:** status `201 Created`. The body returned `body`, `userId` and `"id": 101`.
- **Verdict:** Fails against the expected result (the request was accepted). Needs clarification, because the requirement is undefined. JSONPlaceholder is a fake API that accepts almost anything, so this behaviour is expected here. On a real project, check the API documentation or ask the team before logging a bug.

---

## Status code groups

| First digit | Meaning | Whose problem |
|---|---|---|
| 2xx | Success | nobody's |
| 4xx | The request was wrong | the client |
| 5xx | The server failed | the server |

A missing required field is the client's mistake, so a well-built API returns a 4xx code (such as 400), not 201.

## Automated versions

| Test case | Function in `test_api.py` |
|---|---|
| TC-API-001 | `test_get_existing_user` |
| TC-API-002 | `test_get_missing_user` |
| TC-API-003 | `test_create_post` |
| TC-API-004 | not automated yet |
