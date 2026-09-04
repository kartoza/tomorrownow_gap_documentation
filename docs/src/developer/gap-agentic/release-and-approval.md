---
title: Release and approval
summary: The maker-checker release workflow for farmer-facing advisories and what completion means.
date: 2026-09-04
some_url: https://github.com/kartoza/tomorrownow_gap
copyright: Copyright 2026, TomorrowNow
license: This program is free software; you can redistribute it and/or modify it under the terms of the GNU Affero General Public License as published by the Free Software Foundation; either version 3 of the License, or (at your option) any later version.
---

# Release and approval

A defective advisory can cost a harvest, so releasing farmer-facing advice is a
controlled workflow rather than a single send action. The workflow freezes the
audience, exposes every warning, and separates preparation from approval.

## Maker-checker

The operator who prepares a release cannot approve it, and the reviewer must see
every distinct message variant before it goes out.

1. **Audience** freezes the resolved recipient records; it is not a query re-run
   at send time.
2. **Run** binds an advisory execution to that audience snapshot.
3. **Prepare** reports all failing reasons at once; warnings require an explicit
   decision.
4. **Review** shows every distinct message variant with counts and masked
   identities.
5. **Execute** dispatches through a worker; retries contact only the recipients
   that previously failed.

```mermaid
flowchart LR
    AUD[Audience snapshot] --> RUN[Run]
    RUN --> PREP[Prepare<br/>all warnings surfaced]
    PREP --> REV[Review<br/>every variant]
    REV --> EX[Execute<br/>dispatch + targeted retries]
```

## What "done" means

Release completion means the bundle actually reached its destination, not merely
that it was produced. This matters most with export-style transport: rows written
to a file are only *submitted*; if the file never reaches its pickup location, the
release is still partial. Delivery therefore has explicit outcomes — completed,
withheld, or failed — consistent with the completion semantics described in
[Delivery orchestration](delivery-orchestration.md).

Separation of preparation from approval is a core property of this workflow; see
[Operator consoles](operator-consoles.md) for the role model behind it.
