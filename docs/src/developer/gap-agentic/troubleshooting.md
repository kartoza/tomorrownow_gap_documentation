---
title: Troubleshooting
summary: Common local development and advisory issues, and where to look first.
date: 2026-09-04
some_url: https://github.com/kartoza/tomorrownow_gap
copyright: Copyright 2026, TomorrowNow
license: This program is free software; you can redistribute it and/or modify it under the terms of the GNU Affero General Public License as published by the Free Software Foundation; either version 3 of the License, or (at your option) any later version.
---

# Troubleshooting

This page lists common categories of problem when working locally and where to
look first. It describes symptoms and reasoning rather than environment-specific
commands.

## Start with the advisory's own record

Before reading logs, inspect the advisory itself. The degradation manifest and
the confidence vector usually explain what happened before the logs do: a
recorded degradation names the specific input that was substituted or missing.
See [Observability and degradation](observability.md).

## Common categories

| Symptom | Likely area | Where to look |
| --- | --- | --- |
| No advisory returned | Configuration or health | Confirm the local services and health checks are green; see [Local development](local-development.md). |
| Advice suppressed unexpectedly | Confidence and policy | Check the confidence vector and any uncertainty gate; see [Index and policy engines](index-and-policy-engines.md). |
| Advisory used default inputs | Missing data | Look for a recorded degradation naming the missing input. |
| Result differs between runs | Non-determinism | An identical synthetic input should reproduce; a difference points at a changed input. See [Decision trace and confidence](decision-trace.md). |
| A source appears unavailable | Source failure | A circuit breaker may have opened; the degradation manifest records it. |
| Startup fails after a policy change | Policy configuration | Policy configuration is validated at startup, so a malformed pack fails the deployment rather than a request; see [Index and policy engines](index-and-policy-engines.md). |

## Escalating an issue

If a problem is not explained by the advisory's own record or the categories
above, capture the synthetic input, the resulting advisory package (including its
trace and degradations), and the relevant metrics before escalating, so the issue
can be reproduced deterministically.
