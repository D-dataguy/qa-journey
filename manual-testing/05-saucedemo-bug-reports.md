# Saucedemo Bug Reports

All three bugs were found with the practice account `problem_user` (password `secret_sauce`) on https://www.saucedemo.com. They were logged as Bug issues in Jira (space "QA Testing").

> Each report must contain only what was actually observed. Reproduce each bug once more and confirm every detail before publishing.

---

## BUG-003 (Jira KAN-4): Add to cart button does not work for some products when logged in as problem_user

- **Status:** New
- **Severity:** Medium
- **Priority:** Medium
- **Environment:** Chrome [Chrome version], Windows 11, https://www.saucedemo.com
- **Steps:**
  1. Open https://www.saucedemo.com
  2. Log in as `problem_user` with password `secret_sauce`.
  3. Click Login.
  4. Click Add to cart on Sauce Labs Bolt T-Shirt, Sauce Labs Fleece Jacket and Test.allTheThings() T-Shirt (Red).
- **Expected result:** all selected products are added to the cart.
- **Actual result:** Sauce Labs Bolt T-Shirt, Sauce Labs Fleece Jacket and Test.allTheThings() T-Shirt (Red) are not added to the cart. Other products are added normally.
- **Reproducibility:** 2 of 2 attempts
- **Evidence:** *(screen recording of the failed clicks, plus a screenshot of the cart afterwards; add the file or link)*

---

## BUG-004 (Jira KAN-5): Products page shows the same dog image for every product when logged in as problem_user

- **Status:** New
- **Severity:** Medium
- **Priority:** Low
- **Environment:** Chrome [Chrome version], Windows 11, https://www.saucedemo.com
- **Steps:**
  1. Log in as `problem_user` with password `secret_sauce`.
  2. Look at the product images on the products page.
  3. Click one product to open its detail page.
  4. Go back to the products page and click the next product.
- **Expected result:** the image of each product matches the name of that product.
- **Actual result:** the products page shows a dog image for every product. Each product's detail page shows the correct image.
- **Reproducibility:** 2 of 2 attempts
- **Evidence:** *(screenshot of the products page; screenshot of one detail page)*

---

## BUG-005 (Jira KAN-6): Last name text is typed into the First name field on the checkout information page (problem_user)

- **Status:** New
- **Severity:** High (a customer cannot complete a purchase)
- **Priority:** High
- **Environment:** Chrome [Chrome version], Windows 11, https://www.saucedemo.com
- **Steps:**
  1. Log in as `problem_user` with password `secret_sauce`.
  2. Click Add to cart on any product.
  3. Click the cart icon at the top right.
  4. Click Checkout.
  5. Type `Destiny` in the First name field. *(use the value you actually typed)*
  6. Click the Last name field and type `Test`. *(use the value you actually typed)*
- **Expected result:** First name keeps what was typed, and Last name shows what was typed. The user can continue to the next step.
- **Actual result:** while typing in the Last name field, the First name text disappears and each letter typed appears in the First name field, replacing the previous letter. *(confirm whether the Last name field stays empty)*
- **Reproducibility:** 2 of 2 attempts
- **Evidence:** *(screen recording of the typing, about 15 seconds; a video cannot play in a Markdown file, so upload it to Google Drive and paste the link)*

---

## Notes on severity and priority

- **Severity** is how badly the bug hurts the user. **Priority** is how soon the team should fix it, which is a business decision. A tester suggests a priority, and the team decides.
- Severity is not a default Jira field, so it is written in the description of each ticket.
