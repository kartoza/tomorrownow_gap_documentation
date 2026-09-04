---
title: Glossary
summary: Stable technical terms used across the GAP Agentic developer guide.
date: 2026-09-04
some_url: https://github.com/kartoza/tomorrownow_gap
copyright: Copyright 2026, TomorrowNow
license: This program is free software; you can redistribute it and/or modify it under the terms of the GNU Affero General Public License as published by the Free Software Foundation; either version 3 of the License, or (at your option) any later version.
---

# Glossary

Stable technical terms used across the GAP Agentic developer guide.

| Term | Meaning |
| --- | --- |
| Advisory package | The canonical, structured output of the pipeline, carrying recommendations, supporting detail, and full ancestry. |
| Agrometeorological feature | A quantity derived from raw weather, for example accumulated rainfall over a window. |
| Assessment | One calculator's verdict, together with its confidence. |
| Confidence vector | A multi-axis expression of uncertainty, banded HIGH / MEDIUM / LOW for farmers. |
| DAG | Directed acyclic graph — nodes with directed edges and no cycles; the shape of a decision trace. |
| Decision trace | The graph of typed nodes linking a recommendation back to the signals that produced it. |
| Degradation | A specific, named record that an input was substituted or omitted. |
| FAO-56 | The UN Food and Agriculture Organization standard soil-water-balance method, stepped daily. |
| Go-semantics | The declared meaning of a positive verdict for a given calculator. |
| Handler | An interface-layer component that validates a request and delegates it inward, without performing science. |
| Index calculator | A self-contained component that answers one agronomic question and returns a verdict. |
| MCP | Model Context Protocol — a way to expose capabilities as callable tools over HTTP and JSON. |
| No-blend | The rule that a single named model and statistic are served per country rather than an average of models. |
| Orchestration | The single advisory pipeline that every entry point converges on. |
| Policy pack | Tenant-supplied configuration declaring conflict, suppression, escalation, and uncertainty rules. |
| Signal | A raw input as received, before any derivation. |
| SPW | Suitable Planting Window — an advisory indicating when conditions favour planting. |
| Tenant | One partner organisation with isolated data, configuration, and credentials. |
| Tool | A named, callable capability with a typed contract, exposed through the MCP surface. |
| Uncertainty gate | A confidence threshold below which action advice is withheld. |

For data-platform terms, see the [developer documentation](../index.md).
