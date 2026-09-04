---
title: Running tests
summary: How testing is approached for GAP Agentic and what a change should preserve.
date: 2026-09-04
some_url: https://github.com/kartoza/tomorrownow_gap
copyright: Copyright 2026, TomorrowNow
license: This program is free software; you can redistribute it and/or modify it under the terms of the GNU Affero General Public License as published by the Free Software Foundation; either version 3 of the License, or (at your option) any later version.
---

# Running tests

GAP Agentic relies on automated tests to keep its contracts and its auditability
stable. This page describes what the tests protect and how to think about them;
for the exact commands and test layout, follow the project's own developer
documentation and test suite rather than any fixed command here.

## What the tests protect

- **Contracts.** Interface contracts and typed data shapes must not change
  silently, because callers depend on them.
- **Layering.** Interface components must not contain scientific logic; a change
  that pushes science into an interface should be caught. See
  [Architecture](architecture.md).
- **Determinism and auditability.** Because a decision trace has deterministic
  node identity (see [Decision trace and confidence](decision-trace.md)), an
  unchanged input should produce an unchanged decision, which makes trace
  comparison usable as a regression check.
- **Honest degradation.** A missing input should produce a recorded degradation
  and the appropriate confidence effect, not a silent substitution. See
  [Observability and degradation](observability.md).

## Before proposing a change

Run the relevant tests locally against a healthy
[local environment](local-development.md), confirm the documentation still
builds, and ensure a synthetic [advisory run](running-an-advisory.md) still
returns a valid package. A change that alters advisory behaviour should update or
add the tests that describe the new behaviour.
