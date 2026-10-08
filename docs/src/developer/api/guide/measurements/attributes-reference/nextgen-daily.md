# NextGen daily forecasts

Daily forecasts with a nominal 10-day horizon. Choose the Nigeria identifier for the Nigeria product. Rainfall percentiles describe different parts of the forecast distribution; P75 is not the ensemble mean. Generic humidity mappings can be configured separately from explicit P50/P75 fields. Use the explicit percentile field when that distinction matters.

## `nextgen_forecast`

Catalogue label: **NextGen Forecast  /  Daily  /  10-day**.

Catalogue grid resolution: 4km. Check response coordinates for the actual grid.

| API attribute | Name / meaning | Output unit | Ensemble field |
|---|---|---|---|
| `precip_accum_p10` | Σ hourly intensity per percentile | degree | No |
| `precip_accum_p25` | Σ hourly intensity per percentile | degree | No |
| `precip_accum_p50` | Σ hourly intensity per percentile | degree | No |
| `precip_accum_p90` | Σ hourly intensity per percentile | degree | No |
| `precip_probability_max` | Max hourly PoP over the day | % | No |
| `tmin_c` | Min hourly temperature over the day | °C | No |
| `tmax_c` | Max hourly temperature over the day | °C | No |
| `rh_min_pct` | Min hourly relative humidity over the day | % | No |
| `rh_max_pct` | Max hourly relative humidity over the day | % | No |
| `wind_mean_ms` | Mean hourly wind speed over the day | m/s | No |
| `wind_max_ms` | Max hourly wind speed over the day | m/s | No |
| `gust_max_ms` | Max hourly wind gust over the day | m/s | No |
| `solar_mjm2` | Daily-mean hourly Solar GHI over the day | MJ/m²/day | No |
| `et0_mm` | FAO-56 PM (10 m→2 m wind) + per-country bias-corr (§5) | mm/day | No |
| `et0_raw_mm` | FAO-56 PM, pre-bias-correction (validation) | mm/day | No |
| `precip_accum_p75` | Σ hourly intensity per percentile | degree | No |
| `rh_mean_pct` | Mean hourly relative humidity P50 over the day | % | No |
| `rh_min_pct_p75` | Min hourly relative humidity P75 over the day | % | No |
| `rh_max_pct_p75` | Max hourly relative humidity P75 over the day | % | No |
| `rh_mean_pct_p75` | Mean hourly relative humidity P75 over the day | % | No |
| `rh_max_pct_p50` | Max hourly relative humidity P50 over the day | % | No |
| `rh_min_pct_p50` | Min hourly relative humidity P50 over the day | % | No |
| `rh_mean_pct_p50` | Mean hourly relative humidity P50 over the day | % | No |

## `nigeria_nextgen_daily_forecast`

Catalogue label: **Nigeria NextGen Daily Forecast  /  10-day**.

Catalogue grid resolution: 9km. Check response coordinates for the actual grid.

| API attribute | Name / meaning | Output unit | Ensemble field |
|---|---|---|---|
| `precip_accum_p10` | Σ hourly intensity per percentile | degree | No |
| `precip_accum_p25` | Σ hourly intensity per percentile | degree | No |
| `precip_accum_p50` | Σ hourly intensity per percentile | degree | No |
| `precip_accum_p90` | Σ hourly intensity per percentile | degree | No |
| `precip_probability_max` | Max hourly PoP over the day | % | No |
| `tmin_c` | Min hourly temperature over the day | °C | No |
| `tmax_c` | Max hourly temperature over the day | °C | No |
| `rh_min_pct` | Min hourly relative humidity over the day | % | No |
| `rh_max_pct` | Max hourly relative humidity over the day | % | No |
| `wind_mean_ms` | Mean hourly wind speed over the day | m/s | No |
| `wind_max_ms` | Max hourly wind speed over the day | m/s | No |
| `gust_max_ms` | Max hourly wind gust over the day | m/s | No |
| `solar_mjm2` | Daily-mean hourly Solar GHI over the day | MJ/m²/day | No |
| `et0_mm` | FAO-56 PM (10 m→2 m wind) + per-country bias-corr (§5) | mm/day | No |
| `et0_raw_mm` | FAO-56 PM, pre-bias-correction (validation) | mm/day | No |
| `precip_accum_p75` | Σ hourly intensity per percentile | degree | No |
| `rh_mean_pct` | Mean hourly relative humidity P50 over the day | % | No |
| `rh_min_pct_p75` | Min hourly relative humidity P75 over the day | % | No |
| `rh_max_pct_p75` | Max hourly relative humidity P75 over the day | % | No |
| `rh_mean_pct_p75` | Mean hourly relative humidity P75 over the day | % | No |
| `rh_max_pct_p50` | Max hourly relative humidity P50 over the day | % | No |
| `rh_min_pct_p50` | Min hourly relative humidity P50 over the day | % | No |
| `rh_mean_pct_p50` | Mean hourly relative humidity P50 over the day | % | No |


[Choose another product](../data-products.md) · [Request parameters](../getting-started.md)
