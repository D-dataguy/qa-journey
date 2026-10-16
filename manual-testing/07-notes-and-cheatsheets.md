# Notes and Cheat Sheets

## 1. Verification and validation

- **Verification:** "Are we building the product right?" Check the software against its specification. It is verification whether the test passes or fails.
- **Validation:** "Are we building the right product?" Check that the product meets the user's need. A product can pass every verification and still fail validation.

## 2. SDLC and STLC

The **STLC** (Software Testing Life Cycle):

1. Requirement analysis
2. Test planning
3. Test case design
4. Environment setup
5. Test execution
6. Test closure

Testing starts at step 1, before there is any software. A bug found in a requirement is the cheapest bug to fix.

## 3. Principles of testing

1. Testing shows the presence of bugs, not their absence.
2. Exhaustive testing is impossible, so choose tests by risk and technique.
3. Defects cluster: a few modules hold most of the bugs.
4. Context matters: a banking app is not tested like a game.

## 4. Test scenario vs test case

| | Test scenario | Test case |
|---|---|---|
| Detail | one line, high level | steps, exact data, expected result |
| Answers | "What should I test?" | "How exactly do I test it?" |
| Count | few | many per scenario |

**Test case fields:** ID, title, preconditions, test data, steps, expected result, actual result, label (positive or negative), verdict.
Rules: one purpose per case, write the expected result before running, use exact data, and make cases independent of each other.

## 5. Test log vs bug report

- **Test log:** one line per check, pass or fail.
- **Bug report:** a full write-up, only when actual differs from expected. The log's Bug ID column points to it.

Bug report fields: title (what is wrong and where), environment (browser version, OS, URL), preconditions, steps to reproduce, expected result, actual result, severity, priority, reproducibility, evidence.
Rules: one bug per report, be objective, make it reproducible, write the title last. Use a screenshot when a single frame shows the problem and a short video when movement or timing matters.

## 6. Bug life cycle

New, Assigned, In progress, Fixed, Ready for retest, Retesting, then **Closed** (the bug is gone) or **Reopened** (it goes back to the developer, and the cycle repeats until it passes).

Other states: Rejected / Not a bug, Duplicate, Deferred, Cannot reproduce.

**Jira board columns** on my practice board: New, In Progress, In Review, Done. "Assigned" is the Assignee field, not a column. "In Review" has to cover Fixed, Ready for retest and Retesting, which is why many teams add columns such as "Ready for QA" and "Retesting".

## 7. Types of testing: which one is it?

Ask what just happened that made you test.

| What just happened | Type | The question |
|---|---|---|
| A new build arrived | **Smoke** | Is it alive? (broad and shallow) |
| A small change was made | **Sanity** | Does this change work? (narrow) |
| A bug was marked fixed | **Retesting** | Is that bug gone? (repeat the original steps) |
| Any change was made | **Regression** | Did it break other things? |
| Nothing changed, checking how parts connect | **Integration** | Do these parts work together? |
| The whole product, end to end | **System** | Does the complete product work? |
| A real user or client approves it | **UAT** | Is it the right product for them? |
| A developer's code checks one piece of code | **Unit** | Does this one piece work alone? |

**Functional** testing checks what the system does. **Non-functional** testing checks how well it does it (speed, security, usability, compatibility). Response time is non-functional.

## 8. Agile and Scrum

- **Waterfall:** phases in order (requirements, design, build, test, release), with testing late. **Agile:** small pieces delivered often, with testing in every sprint and early feedback.
- **Sprint:** a fixed period, usually 2 weeks, in which the team completes a set of work.
- **Product backlog:** everything the product might need, in priority order. **Sprint backlog:** what the team chose for this sprint.
- **User story:** *As a [type of user], I want [something] so that [reason].* Example: *As a customer, I want to pay for my order with a card at checkout so that I can complete my purchase without leaving the site.* Stories need wording a tester can check ("pay with a card", not "pay easily").
- **Acceptance criteria:** the conditions a story must meet to count as done. They become test cases.
- **Roles:** Product Owner (what is built), Scrum Master (the process), Developers, Testers (QA).
- **Events:** sprint planning, daily stand-up (15 minutes), sprint review, retrospective. Questions about unclear requirements are raised in planning (or in backlog refinement).

### Worked example: a search story

> **Story:** As a shopper, I want to search for a product so that I can find it quickly.
> **Acceptance criteria:** 1. The search box is on every page. 2. Typing a product name and pressing Enter shows matching products. 3. If no products match, the message "No results found" appears.

Test case titles:

1. Verify that the search box is on every page.
2. Verify that searching for a product name and pressing Enter shows the matching products.
3. Verify that the message "No results found" is displayed when no product matches.
4. Verify the behaviour when a search is submitted with an empty box. *(Requirement gap.)*

Questions for the team:

- What is the maximum acceptable response time for a search? (A requirement without a number cannot be tested.)
- Does the search box have a button, or does it respond only to Enter?
- Does search match partial words (`bag` for `backpack`)?
- Is search case sensitive?

## 9. API basics

| Method | Meaning |
|---|---|
| GET | read data |
| POST | create new data |
| PUT / PATCH | update data (PUT replaces, PATCH changes part of it) |
| DELETE | remove data |

Status codes: 200 OK, 201 Created, 204 No content, 400 Bad request, 401 Unauthorised, 403 Forbidden, 404 Not found, 500 Server error.
A request has a method, a URL (endpoint), headers and sometimes a body (usually JSON).

## 10. Pre-send checklist (my common slips)

- [ ] Search the document for leftover placeholders such as `(version)` and typos such as "chart" for "cart".
- [ ] Do the test data and the steps match exactly? (Check the URL line first.)
- [ ] Is every ID unique?
- [ ] Is every expected result decided from the requirement, not from what the app did?
- [ ] Is every detail something I actually saw?
- [ ] Are labels and verdicts consistent (negative cases are labelled Negative)?
- [ ] Read it aloud once, start to finish.
