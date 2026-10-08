# NeuralGCM S2S

Use neuralgcm_s2s for the catalogue labelled 2021–2025 and neuralgcm_s2s_realtime for realtime forecasts. Select available runs and inspect returned times; the catalogue label does not establish availability for every location or date.

## `neuralgcm_s2s`

Catalogue label: **NeuralGCM S2S  /  2021-2025**.

| API attribute | Name / meaning | Output unit | Ensemble field |
|---|---|---|---|
| `2m_temperature` | 2 meter temperature | K | Yes |
| `2m_dewpoint_temperature` | 2 meter dewpoint temperature | K | Yes |
| `total_precipitation_6hr` | Total precipitation over a 6-hour period | mm/day | Yes |

## `neuralgcm_s2s_realtime`

Catalogue label: **NeuralGCM S2S  /  Realtime**.

| API attribute | Name / meaning | Output unit | Ensemble field |
|---|---|---|---|
| `2m_temperature` | 2 meter temperature | K | Yes |
| `2m_dewpoint_temperature` | 2 meter dewpoint temperature | K | Yes |
| `total_precipitation_6hr` | Total precipitation over a 6-hour period | mm/day | Yes |


[Choose another product](../data-products.md) · [Request parameters](../getting-started.md)

The six-hour precipitation field also carries the catalogue unit `mm/day`. Confirm the response time interval and unit convention before deriving daily totals.
