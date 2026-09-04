---
title: Operator consoles
summary: The source-operations and advisory-operations consoles, and the roles that use them.
date: 2026-09-04
some_url: https://github.com/kartoza/tomorrownow_gap
copyright: Copyright 2026, TomorrowNow
license: This program is free software; you can redistribute it and/or modify it under the terms of the GNU Affero General Public License as published by the Free Software Foundation; either version 3 of the License, or (at your option) any later version.
---

# Operator consoles

The operator product line contains two independently deployable applications over
one shared science and data plane. Naming them by responsibility avoids baking any
one institution's structure into the product.

## Two consoles, one core

- **Source operations** registers, canonicalises, validates, qualifies, and
  exchanges forecast sources. A typical operator is a national meteorological
  service.
- **Advisory operations** selects qualified sources, binds them to use cases,
  runs and reviews advisories, and delivers to farmers. A typical operator is a
  national agricultural research service.

Both live in one product-line codebase and reuse the shared shell, identity,
authorisation, audit, and typed contracts. They deliberately do **not** share
navigation, page composition, workflows, institutional vocabulary, branding, or
geography-specific screens.

```mermaid
flowchart TD
    subgraph Shared core
        ID[Identity · authorization · audit · typed contracts]
    end
    SO[Source operations<br/>govern forecast sources] --> ID
    AO[Advisory operations<br/>run and release advisories] --> ID
```

A product boundary is not a repository boundary: splitting into two codebases
would let them drift apart on security fixes, migrations, session behaviour, and
audit logic.

## Roles and capabilities

Access is expressed as explicitly named **capabilities** rather than reused
generic permissions, so the same label never hides different meanings across
products. Capabilities are namespaced by domain (for example, source-related,
advisory-related, and model-related capabilities), and authorisation is scoped by
actor, capability, organisation, resource, geography, and time. Roles group
capabilities for common operators such as viewer, operator, approver, support,
and administrator.

Separation of duties — ensuring one person cannot control incompatible steps — is
a design goal of this model; see
[Specified vs implemented](specified-vs-implemented.md) for the current status of
its enforcement, and [Release and approval](release-and-approval.md) for how it
applies to farmer-facing releases.
