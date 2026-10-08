# KMSA Kenya daily rainfall forecast

Daily rainfall forecast for Kenya from the **Kenya Meteorological Service Authority (KMSA)**: a downscaled ECMWF extended-range forecast on a 0.05° grid (about 5.5 km), with one rainfall amount per day for lead days 0 to 41 (42 days). It covers Kenya only.

This is a separate rainfall-only product. It has no ensemble members and none of the other weather variables available from NextGen. A missing value means the forecast is unavailable for that cell and day; do not treat it as zero rain. A new run can become available up to two days after its run date.

## `kenya_rainfall_daily`

Catalogue label: **Kenya Rainfall Forecast  /  42-day**.

| API attribute | Name / meaning | Output unit | Ensemble field |
|---|---|---|---|
| `precipitation` | Precipitation | mm | No |


[Choose another product](../data-products.md) · [Request parameters](../getting-started.md)
