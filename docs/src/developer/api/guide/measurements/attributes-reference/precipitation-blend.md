# Daily precipitation forecast

Daily WeatherNext 2 ensemble rainfall statistics with a nominal 14-day horizon. The existing API identifier remains stable. The layer serves 24 weather fields, plus 6 diagnostic fields marked *being removed* below; those are scheduled for removal in kartoza/tomorrownow_gap#1718. Do not build new integrations on them.

## `precipitation_blend_forecast`

Catalogue label: **Precipitation Blend Forecast  /  Daily  /  14-day**.

Catalogue grid resolution: 27.8km. Check response coordinates for the actual grid.

| API attribute | Name / meaning | Output unit | Ensemble field |
|---|---|---|---|
| `blend_p_occurrence` | Fraction (0-1) of ensemble members with daily precipitation >= 0.5 mm. | mm/mm | No |
| `blend_p_heavy` | Fraction (0-1) of ensemble members with daily precipitation >= 20 mm. | mm/mm | No |
| `blend_mean` | Ensemble mean of daily precipitation, in mm. | mm | No |
| `blend_std` | Ensemble standard deviation of daily precipitation, in mm. | mm | No |
| `blend_q10` | 10th percentile of daily precipitation across ensemble members, in mm. | mm | No |
| `blend_q25` | 25th percentile of daily precipitation across ensemble members, in mm. | mm | No |
| `blend_median` | 50th percentile of daily precipitation across ensemble members, in mm. | mm | No |
| `blend_q75` | 75th percentile of daily precipitation across ensemble members, in mm. | mm | No |
| `blend_q90` | 90th percentile of daily precipitation across ensemble members, in mm. | mm | No |
| `blend_iqr` | Difference between the 75th and 25th percentiles of daily precipitation, in mm. | mm | No |
| `blend_p_gt_1mm` | Percentage (0-100) of ensemble members with daily precipitation >= 1 mm. | % | No |
| `blend_p_gt_5mm` | Percentage (0-100) of ensemble members with daily precipitation >= 5 mm. | % | No |
| `blend_p_gt_10mm` | Percentage (0-100) of ensemble members with daily precipitation >= 10 mm. | % | No |
| `blend_p_gt_20mm` | Percentage (0-100) of ensemble members with daily precipitation >= 20 mm. | % | No |
| `blend_p_gt_50mm` | Percentage (0-100) of ensemble members with daily precipitation >= 50 mm. | % | No |
| `blend_w_probability` | Fraction (0-1) of members with daily precipitation >= 0.5 mm; unavailable when fewer than 10 complete member-days are counted. | mm/mm | No |
| `blend_w_p_heavy` | Fraction (0-1) of members with daily precipitation >= 20 mm; unavailable when fewer than 10 complete member-days are counted. | mm/mm | No |
| `blend_event` | 1 when rainfall event probability is >= 0.25, otherwise 0. Check primary for unavailable rainfall. | code | No |
| `blend_heavy` | 1 when heavy rainfall event probability is >= 0.30, otherwise 0. Check primary for unavailable rainfall. | code | No |
| `blend_consensus_mm` | Alias of blend_q75: daily precipitation 75th percentile, in mm. The default precipitation mapping also uses Q75; primary is the separately gated amount. | mm | No |
| `blend_scenario` | 0=no data, 1=dry, 2=marginal, 3=rain, 4=heavy, classified from ensemble occurrence and heavy rainfall probabilities. | code | No |
| `blend_confidence` | Occurrence-probability decisiveness: 0=low, 1=medium, 2=high. 0 also denotes unavailable data (blend_scenario=0). This is not a forecast skill score. | code | No |
| `precipitation` | Precipitation | mm | No |
| `primary` | Daily Q75 when the rainfall event flag is 1, zero for a valid non-event, and unavailable when fewer than 10 complete member-days are counted. | mm | No |
| `blend_model_scenario` | Active model scenario used in the blend (being removed) | code | No |
| `blend_n_models` | Number of models contributing to the blend (being removed) | code | No |
| `blend_w_occ_gc` | GenCast model weight for precipitation occurrence (being removed) | mm/mm | No |
| `blend_w_amt_gc` | GenCast model weight for precipitation amount (being removed) | mm/mm | No |
| `blend_w_amt_heavy_gc` | GenCast model weight for heavy precipitation amount (being removed) | mm/mm | No |
| `blend_w_heavy_gc` | GenCast model weight for heavy precipitation probability (being removed) | mm/mm | No |

## Choosing a rainfall field

- `blend_q75` and `blend_consensus_mm` both return daily Q75. The default `precipitation` mapping also uses Q75, but that mapping is configurable.
- `primary` returns daily Q75 when occurrence probability reaches 0.25, zero for a valid non-event, and unavailable when the member-availability gate fails.
- `blend_p_occurrence` and `blend_p_heavy` are fractions from 0 to 1. `blend_p_gt_*` fields are percentages from 0 to 100 and use **at or above** the named threshold.
- `blend_confidence` describes ensemble decisiveness, not measured forecast skill. Zero can mean low decisiveness or unavailable data; check `blend_scenario`.

The probability metadata may retain `mm/mm` as the unit for fractions. Use the documented 0–1 scale. Missing or incomplete member/time coverage requires care: do not infer a dry day solely from a zero percentile or probability. Check availability and use the returned scenario and gated amount together.

[Choose another product](../data-products.md) · [Request parameters](../getting-started.md)
