# Google WeatherNext 2

An ensemble forecast with a nominal 15-day horizon. Six-hour rainfall amounts refer to their accumulation interval. Preserve the member dimension when analysing uncertainty. Read the returned units; source storage units and API output units can differ.

## `google_weathernext2`

Catalogue label: **Google WeatherNext 2  /  15-day Forecast**.

Catalogue grid resolution: 27.8km. Check response coordinates for the actual grid.

| API attribute | Name / meaning | Output unit | Ensemble field |
|---|---|---|---|
| `total_precipitation_6hr` | Total precipitation over a 6-hour period | mm/day | Yes |
| `10m_u_component_of_wind` | 10 meter U wind component | m/s | Yes |
| `10m_v_component_of_wind` | 10 meter V wind component | m/s | Yes |
| `temperature` | Temperature | °C | Yes |


[Choose another product](../data-products.md) · [Request parameters](../getting-started.md)

## Rainfall units

The catalogue currently labels `total_precipitation_6hr` as `mm/day`, while the field describes a six-hour accumulation. Do not interpret that label as a confirmed daily total or multiply it by six. Inspect response units and time intervals and confirm the convention with GAP before aggregating.
