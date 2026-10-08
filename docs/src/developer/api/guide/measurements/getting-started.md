# Make your first request

## 1. Authenticate

[Create an API key](../api-keys.md) and set it in your local environment:

```bash
export GAP_API_TOKEN='YOUR_API_KEY'
```

Send it as `Authorization: Token YOUR_API_KEY`. Keep the key out of shared notebooks, source control and URLs. Basic authentication with your GAP username and password is also supported over HTTPS.

In the [interactive API](https://gap.tomorrownow.org/api/v1/docs/), use **Authorize**, select an endpoint and choose **Try it out**. The exact authentication controls can differ by deployment.

## 2. Discover products and fields

```bash
curl --fail-with-body --get \
  'https://gap.tomorrownow.org/api/v1/measurement/options/' \
  --header "Authorization: Token $GAP_API_TOKEN"
```

The response contains `products` (each with `variable_name` and `name`) and `attributes` (product identifier to field-name list). Copy exact identifiers into the request. Compare them with the [product catalogue](data-products.md); planned changes may not yet appear in the deployed service.

## 3. Query a point

This example uses IMERG V07 daily satellite rainfall, an observational product, so its dates do not expire with a forecast horizon:

```bash
curl --fail-with-body --get \
  'https://gap.tomorrownow.org/api/v1/measurement/' \
  --header "Authorization: Token $GAP_API_TOKEN" \
  --data-urlencode 'product=imerg_v07' \
  --data-urlencode 'attributes=precipitation' \
  --data-urlencode 'start_date=2026-09-01' \
  --data-urlencode 'end_date=2026-09-03' \
  --data-urlencode 'lat=-1.404244' \
  --data-urlencode 'lon=35.008688' \
  --data-urlencode 'output_type=json'
```

Inspect the returned coordinates, dates, units and missing values. Actual values and coverage depend on the service and your permissions.

## Request parameters

| Parameter | Meaning |
|---|---|
| `product` | Exact product identifier. |
| `attributes` | Comma-separated attribute identifiers for that product. |
| `start_date`, `end_date` | Requested data dates, `YYYY-MM-DD`; TAMSAT normals accept `MM-DD`. |
| `start_time`, `end_time` | Optional UTC times, `HH:MM:SS`. |
| `forecast_date` | Select an archived forecast run where supported: `YYYY-MM-DD`, or `YYYY-MM-DDTHH` for an hourly initialisation. |
| `output_type` | `json`, `csv`, `netcdf` or reader-compatible `ascii`. |
| `lat`, `lon` | A point in WGS84 decimal degrees. Supply both. |
| `bbox` | `west,south,east,north` in WGS84 degrees. |
| `location_name` | Name of a geometry uploaded by your account. |
| `altitudes` | Optional lower and upper altitude bounds for relevant observations. |
| `async` | `true` to submit a background job; otherwise the request waits for a result. |

Choose one location method: point, bounding box or uploaded location. Date-range limits vary by product. Static soil readers may not use dates, but supplying valid dates keeps requests consistent with the documented measurement interface.

## 4. Use a forecast

Choose available valid dates within the selected run's horizon. For example:

| Product | Example fields | Meaning |
|---|---|---|
| `nextgen_forecast` | `precip_accum_p50,precip_accum_p75,tmin_c,tmax_c` | Daily rainfall percentiles and temperature bounds. |
| `nextgen_hourly_forecast` | `precip_intensity_p50,temp_c` | Hourly rainfall rate and temperature. |
| `google_weathernext2` | `total_precipitation_6hr,temperature` | Ensemble rainfall and temperature. |
| `precipitation_blend_forecast` | `primary,blend_q75,blend_scenario` | Gated daily amount, Q75 and availability/event scenario. |

Use Nigeria's dedicated NextGen identifiers for Nigeria. For reproducible comparisons, select `forecast_date` where supported and inspect the response; the requested run is not by itself proof of the provider's actual issuance time.

[Python / Jupyter](../access-api-using-jupyter.md) · [R](../access-api-using-r.md) · [Background jobs and errors](advanced-usage.md)
