---
title: Specified vs implemented
summary: How to read the platform's design as accepted specification versus shipped implementation.
date: 2026-09-04
some_url: https://github.com/kartoza/tomorrownow_gap
copyright: Copyright 2026, TomorrowNow
license: This program is free software; you can redistribute it and/or modify it under the terms of the GNU Affero General Public License as published by the Free Software Foundation; either version 3 of the License, or (at your option) any later version.
---

# Specified vs implemented

Architecture documentation becomes misleading when a planned capability is
described in the present tense as though it already ships. To avoid that, treat
the platform's design as two distinct things: what is **specified** (defined in
an accepted design) and what is **implemented** (present in code and verified).

## How to read the design

- A **specified** capability is an agreed design that may or may not yet exist in
  code.
- An **implemented** capability is present and verified against the current code.
- Some capabilities are **partial**: a subset is implemented while the rest
  remains specified.

When reading any conceptual page in this guide, assume it describes intended
behaviour, and verify specifics against the current code before relying on them —
particularly for governance controls such as separation of duties in the source
approval path, which is a design goal whose enforcement should be confirmed
against the current implementation rather than assumed.

## Why this distinction matters

The platform is deployed in contexts where a control that is only *specified*
cannot be relied upon as though it were *enforced*. Documenting the distinction
keeps onboarding material honest and prevents a plan from being mistaken for a
shipped guarantee. For related governance concepts, see
[Operator consoles](operator-consoles.md) and
[Qualification, adoption, and binding](qualification-adoption-and-binding.md).
