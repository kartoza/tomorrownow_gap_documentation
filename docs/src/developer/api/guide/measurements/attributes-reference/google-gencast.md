---
title: Google Gencast 15-day Forecast
summary: Attributes for Google Gencast 15-day Forecast
  - Zulfikar Akbar Muzakki
date: 2025-12-18
some_url: https://github.com/kartoza/tomorrownow_gap.git
copyright: Copyright 2025, Kartoza
contact:
license: This program is free software; you can redistribute it and/or modify it under the terms of the GNU Affero General Public License as published by the Free Software Foundation; either version 3 of the License, or (at your option) any later version.
---

# Google Gencast 15-day Forecast

> **Note on lead times:** When Google runs the Gencast model between 00:00 to 12:00, it is marked as 12:00. On GAP, the timestamp is adjusted to 00:00, so the lead time is decreased by 12 hours.

| Name | Description | Unit | API attribute name |
|-----|------------|------|--------------------|
| 10 meter U wind component | Zonal (west–east) component of wind measured at 10 meters above ground | m/s | 10m_u_component_of_wind |
| 10 meter V wind component | Meridional (south–north) component of wind measured at 10 meters above ground | m/s | 10m_v_component_of_wind |
| 2 meter temperature | Air temperature measured at 2 meters above ground level | K | 2m_temperature |
| Total precipitation over a 12-hour period | Total accumulated precipitation over a 12-hour period | m | total_precipitation_12hr |