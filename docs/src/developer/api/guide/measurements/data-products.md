---
title: GAP Data Products
summary: Available weather and climate data products
  - Irwan Fathurrahman
date: 2024-06-18
some_url: https://github.com/kartoza/tomorrownow_gap.git
copyright: Copyright 2024, Kartoza
contact:
license: This program is free software; you can redistribute it and/or modify it under the terms of the GNU Affero General Public License as published by the Free Software Foundation; either version 3 of the License, or (at your option) any later version.
---

# GAP Input Data Table

## Historical Data
| Product | Provider | Resolution | Source | Version | API product_type |
|---------|----------|------------|--------|---------|------------------|
| CBAM Daily Reanalysis (Raw) 2012-2024 v2 | Tomorrow.io | 4km x 4km | Tomorrow.io CBAM 1F enhanced bias-corrected reanalysis | 2012-2024 v2 | cbam_historical_analysis |
| CBAM Daily Reanalysis (Bias-Corrected) 2012-2023 v1 | Tomorrow.io | 4km x 4km | Tomorrow.io CBAM 1F enhanced bias-corrected reanalysis | 2012-2023 v1 | cbam_historical_analysis_bias_adjust |
| Automated Weather Stations (TAHMO) (QC/QA) 2018 - 2025 v1 | TAHMO weather stations | 300+ stations across East Africa | TAHMO Gap Filled Data (csv) | 2018-2025 v1 | tahmo_ground_observation |
| Automated Weather Stations (Arable) 2024-2025 | Arable weather stations | 300+ stations across East Africa | Arable (API) | 2024-2025 | arable_ground_observation |
| Disdrometer (Laser Rain Gauge) | disdrometers | | Tahmo (API) | | disdrometer_ground_observation |
| Radiosonde Observations (Windborne) | WindBorne Systems | 100 weather balloons | Windborne Systems | | windborne_radiosonde_observation |
| TAMSAT Precipitation Long-term Normals (20-year) | TAMSAT | | | | tamsat_ltn |
| Google Gencast | Google | 27830m | Google WeatherNext Gen Forecasts | | google_gencast |
| Google Graphcast | Google | 27830m | Google WeatherNext Graph Forecasts | | google_graphcast |


## Weather Forecasts
| Product | Provider | Resolution | Source | Version | API product_type |
|---------|----------|------------|--------|---------|------------------|
| CBAM Weather Forecast Daily 10-day | Tomorrow.io | 4km x 4km | Tomorrow.io CBAM satellite enhanced short-term weather forecasts | | cbam_shortterm_forecast |
| CBAM Weather Forecast Hourly 4-day | Tomorrow.io | 4km x 4km | Tomorrow.io CBAM satellite enhanced short-term weather forecasts | | cbam_shortterm_hourly_forecast |
| Salient Predictions Weather Forecast - Sub-seasonal to Seasonal (8-month) | Salient | 28km x 28km | Salient (API) | v9 | salient_seasonal_forecast |
| Salient Predictions Weather Forecast - GEMv2 (3-month) | Salient | 28km x 28km | Salient (API) | v9 | salient_gemv2_forecast |
| Google Gencast | Google | 27830m | Google WeatherNext Gen Forecasts | | google_gencast |
| Google Graphcast | Google | 27830m | Google WeatherNext Graph Forecasts | | google_graphcast |
| Google Nowcast | Google | 5km x 5km |  | | google_nowcast |

> **Note:** The Today value from the CBAM short term weather forecast is stored and can be accessed for historical records dating back to 12 October 2024.

> **Note on Google Gencast and Graphcast lead times:** When Google runs the Gencast model between 00:00 to 12:00, it is marked as 12:00. On GAP, the timestamp is adjusted to 00:00, so the lead time is decreased by 12 hours. The same applies to Graphcast, but with a 6-hour adjustment.
