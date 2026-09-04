---
title: Sovereign deployment
summary: What a sovereign GAP deployment is, and how it differs from source governance.
date: 2026-09-04
some_url: https://github.com/kartoza/tomorrownow_gap
copyright: Copyright 2026, TomorrowNow
license: This program is free software; you can redistribute it and/or modify it under the terms of the GNU Affero General Public License as published by the Free Software Foundation; either version 3 of the License, or (at your option) any later version.
---

# Sovereign deployment

"Sovereign" is used for two related but distinct ideas in GAP. Keeping them
separate avoids confusion in architecture and product discussions.

## Two meanings

1. **A sovereign runtime** is a *deployment shape*: an agency-hosted, locally
   controlled, offline-capable instance that makes no required call back to
   TomorrowNow services. The agency controls its data, models, workflows, and
   the timing of its own upgrades.
2. **Source governance** is a *software capability*: the admission, validation,
   qualification, and exchange of forecast sources.

An organisation can run a sovereign runtime without operating source governance,
so "sovereign" should never be treated as shorthand for a particular console.

```mermaid
flowchart LR
    R[Sovereign runtime<br/>agency-hosted, offline-capable] --- S[Source governance<br/>admit · validate · qualify]
    R --> O[Locally controlled outcomes]
```

## Why sovereignty shapes the architecture

The goal is that a country can run its own instance, on its own infrastructure,
under its own data rules, choosing its own thresholds and upgrade timing. That
goal drives design decisions that would otherwise look unusual: offline-capable
deployments, no dependency on external content-delivery networks, and portable,
signed qualification bundles so that governance decisions can travel to an
offline installation.

The shared platform core stays interoperable through stable APIs rather than
country-specific forks, so security fixes and migrations apply everywhere without
diverging per country. See [Operator consoles](operator-consoles.md) for how
responsibilities divide across institutions, and
[Qualification, adoption, and binding](qualification-adoption-and-binding.md) for
how source governance travels between organisations.
