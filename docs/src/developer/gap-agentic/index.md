---
title: GAP Agentic
summary: An overview of the GAP Agentic advisory platform and how it relates to GAP v1.
date: 2026-09-04
some_url: https://github.com/kartoza/tomorrownow_gap
copyright: Copyright 2026, TomorrowNow
license: This program is free software; you can redistribute it and/or modify it under the terms of the GNU Affero General Public License as published by the Free Software Foundation; either version 3 of the License, or (at your option) any later version.
---

# GAP Agentic

**GAP Agentic** is the reasoning layer of the Global Access Platform (GAP). Where
GAP v1 curates weather and climate data and serves it through APIs, GAP Agentic
turns that data into per-request agronomic advice: it reasons over the current
context for a location and returns a recommendation together with the evidence
and confidence behind it.

For the underlying data platform, datasets, and public APIs, see the existing
[developer architecture](../architecture.md) and
[API guide](../api/guide/index.md).

## What "agentic" means here

Agentic does not mean "a language model writes the advisory". It means the system
**reasons over context per request** rather than firing a fixed rule on a
schedule. For a given request it consults the relevant forecast, calibration, and
validation signals, evaluates them against a decision engine, and reports three
things together:

- what it recommends,
- the evidence chain that produced the recommendation, and
- how confident it is, including where data was missing.

That last point is a design requirement: the platform is expected to be explicit
about its own uncertainty rather than presenting a confident guess.

## How it relates to GAP v1

| Concern | GAP v1 | GAP Agentic |
| --- | --- | --- |
| Primary job | Curate and serve weather/climate data | Reason over that data to produce advice |
| Interaction | Data queries and downloads | Per-request or scheduled advisory preparation |
| Output | Datasets and measurements | An auditable advisory package |

GAP Agentic is additive: it builds on the same data foundation and does not
replace the data APIs.

## Two commitments

Two principles run through the whole platform and are worth stating up front:

1. **Every advisory is auditable.** No recommendation exists without a traceable
   chain back to the signals that produced it. See
   [Decision trace and confidence](decision-trace.md).
2. **The system degrades honestly.** When data is missing or a source is
   unavailable, the platform records that in a structured way rather than
   silently substituting a guess. See [Observability and degradation](observability.md).

## Where to go next

- [Architecture](architecture.md) — the layered platform and its responsibility
  boundaries.
- [Advisory lifecycle](advisory-lifecycle.md) — how a request becomes an
  advisory.
- [Index and policy engines](index-and-policy-engines.md) — how agronomic
  questions are answered and reconciled.
- [Glossary](glossary.md) — stable technical terms used across these pages.
