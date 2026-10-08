# Product changes

Reviewed 8 October 2026. The following removals are prepared for the API release; rollout is still pending. Stop using these identifiers for new integrations. The running service may show them until that release is deployed.

| Legacy identifier | Guidance |
|---|---|
| `google_gencast`, `google_gencast_2_nigeria` | Move to `google_weathernext2` (or `nigeria_nextgen_daily_forecast` for Nigeria) after checking attributes, units, intervals and coverage. `google_gencast_2_nigeria` is still served until the retirement is deployed; see [legacy products](data-products.md#legacy-products). |
| `cbam_shortterm_forecast`, `cbam_shortterm_hourly_forecast` | Evaluate `nextgen_forecast` or `nextgen_hourly_forecast`; the field names and statistical meaning differ. |
| `nigeria_daily_forecast`, `nigeria_hourly_forecast` | Evaluate `nigeria_nextgen_daily_forecast` or `nigeria_nextgen_hourly_forecast`. |
| `cbam_historical_analysis`, `cbam_historical_analysis_bias_adjust` | Still served; listed under [legacy products](data-products.md#legacy-products). For new historical rainfall work use `imerg_v07`. |

After deployment, new requests for these retired products return HTTP 410. These are not simple name substitutions: update and validate your queries against each new product's field reference.

The daily precipitation layer `precipitation_blend_forecast` keeps its identifier and 24 weather fields. Six diagnostic fields (`blend_model_scenario`, `blend_n_models` and four `blend_w_*_gc` GenCast weights) are still served and are marked *being removed*; they will be dropped when kartoza/tomorrownow_gap#1718 is deployed. Existing rainfall aliases remain.

The active guide also omits catalogue entries that are inactive or internal: GraphCast, Nowcast, Salient forecasts and hourly CBAM reanalysis. Their omission is not a new retirement of the underlying data or internal workflows.

NextGen, Nigeria NextGen, WeatherNext 2, KMSA Kenya rainfall and FOCUS/1F are preserved. Existing issued exports are not revoked by the public catalogue cleanup.

[Current product catalogue](data-products.md)
