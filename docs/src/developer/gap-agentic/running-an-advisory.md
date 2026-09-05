---
title: Running an advisory
summary: What a local synthetic advisory is and how to read its output.
date: 2026-09-04
some_url: https://github.com/kartoza/tomorrownow_gap
copyright: Copyright 2026, TomorrowNow
license: This program is free software; you can redistribute it and/or modify it under the terms of the GNU Affero General Public License as published by the Free Software Foundation; either version 3 of the License, or (at your option) any later version.
---

# Running an advisory

Once a [local development](local-development.md) environment is healthy, the
canonical check is to produce a **synthetic advisory**: an advisory generated from
non-production data for a chosen location and crop context. It exercises the whole
pipeline end to end without touching real farmer data.

## What a run should produce

A successful run returns an auditable advisory package. When inspecting it, look
for the signals that confirm the pipeline behaved correctly:

- a recommendation for the requested location and context;
- the decision trace linking the recommendation back to its inputs (see
  [Decision trace and confidence](decision-trace.md));
- a confidence vector, banded for readability;
- any degradations recorded on the advisory, if inputs were missing (see
  [Observability and degradation](observability.md)).

```mermaid
flowchart LR
    REQ[Location + crop context] --> PIPE[Advisory pipeline]
    PIPE --> PKG[Advisory package]
    PKG --> CHK[Recommendation + trace + confidence + degradations]
```

## Reading the result

Compare the output against a known-good expected result for the same synthetic
input. Because trace-node identity is deterministic (see
[Decision trace and confidence](decision-trace.md)), an identical input should
produce an identical decision, so any difference is meaningful and worth
investigating. For the phases a request passes through, see the
[advisory lifecycle](advisory-lifecycle.md).

The exact command to invoke a local advisory belongs with the code; follow the
project's own developer documentation for the current invocation.
