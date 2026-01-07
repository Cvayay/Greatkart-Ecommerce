# Software Testing Guide

This document explains the Software Testing Life Cycle (STLC) in detail, shows how Verification and Validation (V&V) fit into STLC, and compares Black Box, White Box and Grey Box testing in plain, human-friendly language with examples, pros/cons and when to use each.

## Table of Contents

- STLC — Overview
- STLC — Detailed Phases
  - Test Planning
  - Test Design
  - Test Environment Setup
  - Test Execution
  - Defect Reporting
  - Test Closure
- Verification vs Validation in STLC
- Testing Types: Comparison
  - Black Box Testing
  - White Box Testing
  - Grey Box Testing
- Quick Decision Guide: Which testing to use when
- Example Test Cases (short)
- Summary

---

## STLC — Overview

The Software Testing Life Cycle (STLC) is a set of defined activities that testing teams perform to ensure software quality. STLC is iterative and aligns with the software development process — each release or sprint runs through the same STLC stages. The STLC focuses on planning, design, environment setup, execution, defect handling, and closure.

Key goals:
- Plan testing work and resources.
- Design effective test cases that cover requirements.
- Set up an environment that reproduces production behaviour.
- Execute tests and report defects clearly.
- Close testing with measurable results and lessons learned.

## STLC — Detailed Phases

1) Test Planning

- Purpose: Decide "what" to test, "who" will do it, and "how" it will be tested.
- Activities:
  - Review requirements and specs.
  - Identify testing scope and objectives.
  - Estimate effort, resources and schedule.
  - Select tools (test management, automation frameworks, CI integration).
  - Define entry and exit criteria for testing phases.
- Output artifacts: Test Plan document, resource plan, risk assessment, test schedule.

2) Test Design

- Purpose: Convert requirements into concrete test cases and test data.
- Activities:
  - Create test scenarios and test cases (positive, negative, boundary).
  - Map test cases to requirements (traceability matrix).
  - Design test data sets and identify any required mocks or stubs.
  - Decide which tests to automate and which to run manually.
- Output artifacts: Test Cases, Test Data, Traceability Matrix, Automation plan.

3) Test Environment Setup

- Purpose: Prepare infrastructure that closely mimics production for meaningful results.
- Activities:
  - Provision servers, databases, networking, and external service mocks.
  - Configure test accounts, sample data, test doubles (mocks/stubs).
  - Validate the environment against requirements (smoke tests).
- Output artifacts: Environment checklist, access credentials (securely stored), smoke test results.

4) Test Execution

- Purpose: Run test cases, record results, and reproduce defects.
- Activities:
  - Execute manual test cases and automation suites.
  - Log results (pass/fail) and attach evidence (screenshots, logs).
  - Re-run failed cases after fixes and perform regression checks.
- Output artifacts: Test execution report, automated test run logs, updated traceability.

5) Defect Reporting

- Purpose: Record issues in a clear, reproducible manner and track their resolution.
- Activities:
  - Log defects with steps to reproduce, expected vs actual, severity and priority.
  - Triage defects with developers and stakeholders.
  - Track defect lifecycle: New → Assigned → Fixed → Verified → Closed.
- Output artifacts: Defect reports/tickets (Jira, GitHub Issues), defect metrics (open/closed, mean time to resolve).

6) Test Closure

- Purpose: Formally end the testing phase and record lessons.
- Activities:
  - Verify exit criteria met (all planned tests executed, critical bugs closed or deferred).
  - Produce test summary report and metrics (coverage, pass rate, outstanding risks).
  - Archive test artifacts and test data; do a lessons-learned review.
- Output artifacts: Test Summary Report, Recommendations, Archived artifacts.

---

## Verification vs Validation in STLC

- Verification (Are we building the product right?):
  - Focus: Process and intermediate artifacts (requirements, design, code reviews).
  - Examples: Requirement reviews, design inspections, static code analysis, unit tests.
  - Where in STLC: Primarily during Test Planning and Test Design, and continues throughout as checks on artifacts.

- Validation (Are we building the right product?):
  - Focus: Behaviour and end-user value — validate the product meets user needs.
  - Examples: System tests, user acceptance testing (UAT), end-to-end scenarios.
  - Where in STLC: Most active during Test Execution and Test Closure when running system-level tests and UAT.

Both are complementary: verification ensures we follow correct development processes and produce correct intermediate outputs; validation ensures the final product meets stakeholder needs.

---

## Testing Types: Comparison

Below are plain-language explanations, techniques, examples and pros/cons for the three common testing approaches.

### Black Box Testing

- What it is: Testing based on requirements and functionality without knowledge of internal implementation. The tester interacts with the system as an external user would.
- Typical activities: Functional testing, boundary value testing, equivalence partitioning, usability testing, acceptance testing.
- Who performs it: QA testers, product owners, or end users (for UAT).
- When to use: System/integration testing, acceptance tests, when validating behaviour against requirements.
- Pros:
  - Tests from user perspective; good for catching functional gaps.
  - No need for developer-specific knowledge; easier to write cross-functional tests.
  - Helps validate requirements and user stories.
- Cons:
  - Potential for incomplete coverage of internal logic (missed branches).
  - Harder to design exhaustive tests for complex logic.
- Example test case (e-commerce):
  - "As a buyer, add a product with variations to the cart, proceed to checkout and complete the order." Expect order confirmation.

### White Box Testing (aka Glass Box / Structural Testing)

- What it is: Testing with knowledge of the internal code structure. Test cases exercise specific paths, conditions, loops and internal logic.
- Typical activities: Unit testing, code coverage analysis, path testing, branch coverage, control-flow testing.
- Who performs it: Developers or testers with code access.
- When to use: Unit testing during development, integration testing where internal logic is vital, security testing.
- Pros:
  - Can achieve high code coverage and exercise internal logic systematically.
  - Useful to find hidden errors in algorithms, boundary handling, and performance hotspots.
  - Enables fine-grained tests and easier debugging when a test fails.
- Cons:
  - Tests tied to implementation; refactoring can break tests even if behaviour unchanged.
  - Requires programming skills and knowledge of internal modules.
- Example test case (e-commerce):
  - Unit test for `calculate_price(product, variations)` ensuring price modifiers are applied correctly for a specific variation combination.

### Grey Box Testing

- What it is: Hybrid approach where tester has limited knowledge of internal structure (e.g., design docs, database schema) but mostly tests via interfaces. It blends external behaviour checks with selective internal checks.
- Typical activities: Integration tests that validate interactions between components, security tests using knowledge of data flow, API testing with schema awareness.
- Who performs it: Experienced testers or engineers who understand both business flows and system internals.
- When to use: Integration testing, system-level testing with focus on data flows, security and compatibility tests.
- Pros:
  - Balances the strengths of Black and White Box methods: better targeted tests, fewer blind spots.
  - Useful for systems where full white-box testing isn't practical but some internal knowledge helps.
- Cons:
  - Requires some internal knowledge and access, which might not always be available.
  - Can still miss deep internal logic bugs if the limited knowledge is insufficient.
- Example test case (e-commerce):
  - Run API calls to place an order while also verifying DB records (order row created, stock decremented) using knowledge of DB schema.

---

## Quick Decision Guide: Which testing to use when

- During development (component/unit): Use White Box (unit tests, code checks).
- When validating feature behaviour and acceptance: Use Black Box (functional tests, UAT).
- For integration, security, or targeted data/flow checks: Use Grey Box.
- For performance and load: Use Black Box style scenarios (simulate users) and also consider internal profiling (White Box) for bottlenecks.

## Example Test Cases (short)

- Black Box example: "Verify login with valid email and password leads to dashboard; invalid credentials show proper error." (No code knowledge required.)
- White Box example: Unit test for `merge_carts(session_items, user_cart)` verifying duplicate detection and quantity aggregation for matching variation sets.
- Grey Box example: Submit order via UI or API then query DB to ensure `Order` and `OrderProduct` rows exist and stock reduced by ordered quantity.

## Summary

- STLC provides a structured approach to testing: plan, design, prepare environment, execute tests, report defects and close.
- Verification and Validation are both crucial: verification focuses on correctness of artifacts/process; validation focuses on correctness of final product behaviour.
- Black Box, White Box and Grey Box testing each have specific roles: choose based on the testing goal (behaviour vs internal logic vs integration/data flow).

---

File location: `TESTING_GUIDE.md` in project root.
