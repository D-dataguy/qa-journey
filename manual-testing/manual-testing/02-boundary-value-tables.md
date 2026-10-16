# Equivalence Partitioning and Boundary Value Analysis

## The method

- **Equivalence partitioning (EP):** group inputs the software should treat the same way, then test one value from each group.
- **Boundary value analysis (BVA):** bugs cluster at the edges of each group, so test just outside, on, and just inside each edge.
- **Deciding the expected result:** ask "can I decide pass or fail using only what the requirement says?" If yes, give a firm result. If no, mark it **Gap** and ask the team. Where a row has both a firm result and an open question, give both.
- Also ask four questions of any field: what if it is **empty**, the **wrong type**, **too big or too small**, or in a **format nobody expected**?

---

## 1. Password: "between 8 and 20 characters"

| Partition | Lengths | Expected |
|---|---|---|
| Invalid (too short) | 0 to 7 | Rejected |
| Valid | 8 to 20 | Accepted |
| Invalid (too long) | 21 and above | Rejected |

| Edge | Just outside | On the edge | Just inside |
|---|---|---|---|
| Lower (8) | 7 | 8 | 9 |
| Upper (20) | 21 | 20 | 19 |

Test values: 7, 8, 9, 19, 20, 21, plus one mid-range value such as 12. See `01-signup-form-test-cases.md` for the written cases (the 19-character case is not written yet).

---

## 2. Age: "between 18 and 60 years old, inclusive"

| Partition | Ages | Expected |
|---|---|---|
| Invalid (too young) | 0 to 17 | Rejected |
| Valid | 18 to 60 | Accepted |
| Invalid (too old) | 61 and above | Rejected |

| Value | Partition | Expected result |
|---|---|---|
| 17 | Invalid (too young) | Rejected |
| 18 | Valid | Accepted |
| 19 | Valid | Accepted |
| 35 | Valid (mid-range) | Accepted |
| 59 | Valid | Accepted |
| 60 | Valid | Accepted |
| 61 | Invalid (too old) | Rejected |

Inputs that are not whole ages at all:

| Input | What it tests | Expected result |
|---|---|---|
| `abc` | Letters in a numeric field | Rejected |
| `-5` | Negative number | Rejected |
| `99999999999` | Extremely large number | Rejected |
| (empty) | Field left blank | **Gap**: the requirement does not say whether the field is mandatory |
| `25.5` | Decimal instead of a whole number | **Gap** |
| `   ` (spaces only) | Whitespace | **Gap** |
| `2e1` | Scientific notation (equals 20) | **Gap** |

---

## 3. Phone number: "Enter your 11-digit phone number"

The numbers below are made-up examples.

| Input | Digits | What it tests | Expected result |
|---|---|---|---|
| `08012345678` | 11 | Valid number | Accepted |
| `0801234567` | 10 | One digit short | Rejected |
| `080123456789` | 12 | One digit too many | Rejected |
| `2348012345678` | 13 | International format without `+` | Rejected, plus **Gap**: was international format intended? |
| `+2348012345678` | 13 plus `+` | International format with `+` | Rejected, plus **Gap**: was international format intended? |
| `0801234abcd` | 11 characters | Letters mixed into the number | Rejected |
| `teste@hma.com` | n/a | An email instead of a number | Rejected |
| `0801 234 5678` | 11 digits with spaces | Formatting characters | **Gap**: are spaces or dashes allowed? |
| (empty) | 0 | Field left blank | **Gap**: is the field mandatory? |

---

## 4. Username: "3 to 15 characters long"

| Input | Length | Expected result | Why |
|---|---|---|---|
| `ab` | 2 | Rejected | Below the minimum of 3 |
| `abc` | 3 | Accepted | On the lower edge |
| `abcdefghijklmno` | 15 | Accepted | On the upper edge |
| `abcdefghijklmnop` | 16 | Rejected | Above the maximum of 15 |
| `john doe` | 8 | Accepted by the length rule, plus **Gap** | The requirement says nothing about whether spaces are allowed |
| `john_99!` | 8 | Accepted by the length rule, plus **Gap** | The requirement does not say whether `_` and `!` are allowed |
| (empty) | 0 | Rejected | Zero characters breaks the minimum of 3 |

A rule only decides what it talks about. This one talks about length and nothing else.
