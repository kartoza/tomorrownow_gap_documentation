---
title: Caching and multi-tenancy
summary: Tenant isolation, cache identity, and safe reuse in GAP Agentic.
date: 2026-09-04
some_url: https://github.com/kartoza/tomorrownow_gap
copyright: Copyright 2026, TomorrowNow
license: This program is free software; you can redistribute it and/or modify it under the terms of the GNU Affero General Public License as published by the Free Software Foundation; either version 3 of the License, or (at your option) any later version.
---

# Caching and multi-tenancy

Multi-tenancy in GAP Agentic is not just a feature; it is a **safety boundary**.
One partner seeing another partner's farmer data would be a breach, so the
architecture makes isolation structural rather than a matter of convention.

## Persistence and caching

A relational database is the authoritative store — the database of record.
Caching runs in separate namespaces, for example one for whole advisory bundles
and one for upstream source responses, backed by an in-memory store in
development and a shared cache in production.

## The tenant rule

Every cache key includes a **tenant identifier**. Tenants therefore never share a
cached response, and a cache key built without a tenant would be a cross-tenant
data leak rather than a mere performance bug. This is a hard isolation boundary
that the code is structured to make difficult to cross by accident.

```mermaid
flowchart TD
    REQ[Request] --> T1{Explicit parameter?}
    T1 -->|no| T2{Tenant header?}
    T2 -->|no| T3{Session tenant?}
    T3 -->|no| T4{Configured default?}
    T4 -->|no| T5[fallback default]
    T1 -->|yes| TEN[tenant resolved]
    T2 -->|yes| TEN
    T3 -->|yes| TEN
    T4 -->|yes| TEN
    T5 --> TEN
    TEN --> CK["Cache key always includes the tenant"]
    CK --> AC[(Advisory cache)]
    CK --> PC[(Source cache)]
    TEN --> DB[(Database of record)]
```

## Tenant resolution

The tenant is resolved from the request in a defined order of precedence — for
example an explicit parameter, then a request header, then the session, then a
configured default, and finally a fallback default for local development. Because
a fallback exists, an unset tenant resolves rather than erroring; in a
multi-tenant deployment the tenant should always be supplied explicitly.

## What a tenant can override

A tenant is a partner with its own configuration, calibration, credentials, and
locale scope. Depending on deployment, a tenant may override values such as
weighting, per-zone thresholds, locale preferences, source credentials, and which
advisory types are enabled. This is the same configuration surface used by the
[policy engine](index-and-policy-engines.md) to let partners shape behaviour
without changing platform code.
