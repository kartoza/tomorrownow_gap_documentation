# NextGen hourly forecasts

Hourly forecasts with a nominal 4-day horizon. Rainfall intensity is a rate in mm/h; daily rainfall accumulation uses mm. Do not add rates without accounting for each time interval.

## `nextgen_hourly_forecast`

Catalogue label: **NextGen Forecast  /  Hourly  /  4-day**.

Catalogue grid resolution: 4km. Check response coordinates for the actual grid.

| API attribute | Name / meaning | Output unit | Ensemble field |
|---|---|---|---|
| `precip_intensity_p10` | The 10th percentile forecast of precipitation intensity | mm | No |
| `precip_intensity_p25` | The 25th percentile forecast of precipitation intensity | mm | No |
| `precip_intensity_p50` | The 50th percentile forecast of precipitation intensity | mm | No |
| `precip_intensity_p90` | The 90th percentile forecast of precipitation intensity | mm | No |
| `precip_probability` | Precipitation Probability | % | No |
| `temp_c` | Temperature deterministic P50 | °C | No |
| `rh_pct` | Relative humidity deterministic P50 | % | No |
| `wind_ms` | Wind speed deterministic P50 | m/s | No |
| `gust_ms` | Wind gust deterministic P50 | m/s | No |
| `solar_wm2` | Solar GHI deterministic | W/m2 | No |
| `precip_intensity_p75` | The 75th percentile forecast of precipitation intensity | mm | No |
| `rh_pct_p75` | Relative humidity deterministic P75 | % | No |
| `rh_pct_p50` | Relative humidity deterministic P50 | % | No |

## `nigeria_nextgen_hourly_forecast`

Catalogue label: **Nigeria NextGen Hourly Forecast  /  4-day**.

Catalogue grid resolution: 9km. Check response coordinates for the actual grid.

| API attribute | Name / meaning | Output unit | Ensemble field |
|---|---|---|---|
| `precip_intensity_p10` | The 10th percentile forecast of precipitation intensity | mm | No |
| `precip_intensity_p25` | The 25th percentile forecast of precipitation intensity | mm | No |
| `precip_intensity_p50` | The 50th percentile forecast of precipitation intensity | mm | No |
| `precip_intensity_p90` | The 90th percentile forecast of precipitation intensity | mm | No |
| `precip_probability` | Precipitation Probability | % | No |
| `temp_c` | Temperature deterministic P50 | °C | No |
| `rh_pct` | Relative humidity deterministic P50 | % | No |
| `wind_ms` | Wind speed deterministic P50 | m/s | No |
| `gust_ms` | Wind gust deterministic P50 | m/s | No |
| `solar_wm2` | Solar GHI deterministic | W/m2 | No |
| `precip_intensity_p75` | The 75th percentile forecast of precipitation intensity | mm | No |
| `rh_pct_p75` | Relative humidity deterministic P75 | % | No |
| `rh_pct_p50` | Relative humidity deterministic P50 | % | No |


[Choose another product](../data-products.md) · [Request parameters](../getting-started.md)
