# Google GenCast — Nigeria (legacy)

> **Legacy product, retirement planned.** Still served today; scheduled for retirement in kartoza/tomorrownow_gap#1717. Use [NextGen Nigeria](nextgen-daily.md) (`nigeria_nextgen_daily_forecast`) for new work.

An ensemble forecast for Nigeria with a nominal 15-day horizon. Preserve the member dimension when analysing uncertainty. Read the returned units; source storage units and API output units can differ.

## `google_gencast_2_nigeria`

Catalogue label: **Google Gencast 2  /  15-day Forecast  /  Nigeria**.

| API attribute | Name / meaning | Output unit | Ensemble field |
|---|---|---|---|
| `total_precipitation_6hr` | Total precipitation over a 6-hour period | mm/day | Yes |
| `10m_u_component_of_wind` | 10 meter U wind component | m/s | Yes |
| `10m_v_component_of_wind` | 10 meter V wind component | m/s | Yes |
| `2m_temperature` | 2 meter temperature | K | Yes |


[Choose another product](../data-products.md) · [Request parameters](../getting-started.md)

## Rainfall units

The catalogue labels `total_precipitation_6hr` as `mm/day` although the field describes a six-hour accumulation. Inspect response units and time intervals before aggregating.
