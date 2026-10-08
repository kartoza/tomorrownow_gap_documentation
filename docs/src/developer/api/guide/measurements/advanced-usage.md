# Advanced usage

## Upload a location

Upload a GeoJSON, GeoPackage or zipped shapefile in WGS84 (EPSG:4326). Supported geometries include points, multipoints, polygons and multipolygons. Put shapefile components at the root of the ZIP, including the `.shp`, `.shx`, `.dbf` and CRS definition.

```bash
curl --fail-with-body \
  'https://gap.tomorrownow.org/api/v1/location/?location_name=my_fields' \
  --header "Authorization: Token $GAP_API_TOKEN" \
  --form 'file=@fields.geojson'
```

Use `location_name=my_fields` in subsequent GET measurement requests instead of `lat`/`lon` or `bbox`. Locations belong to the uploading account. Read `expired_on` in the upload response and re-upload after expiry. For multiple points or polygons use CSV or NetCDF; JSON is restricted to a single point query.

## Submit a background request

Add `async=true` to a normal GET measurement request. A successful submission returns HTTP 200 with a `job_id`; it does not mean the data is ready.

```bash
curl --fail-with-body --get \
  'https://gap.tomorrownow.org/api/v1/measurement/' \
  --header "Authorization: Token $GAP_API_TOKEN" \
  --data-urlencode 'product=imerg_v07' \
  --data-urlencode 'attributes=precipitation' \
  --data-urlencode 'start_date=2026-09-01' \
  --data-urlencode 'end_date=2026-09-03' \
  --data-urlencode 'bbox=36.7,-1.4,36.9,-1.2' \
  --data-urlencode 'output_type=netcdf' \
  --data-urlencode 'async=true'
```

Poll `GET /api/v1/measurement/job-status/{job_id}/` with the same authentication. Wait a few seconds between requests and impose a timeout. `Pending`, `Queued` and `Running` are in-progress states. `Completed` returns `url` for a file or `data` for JSON. Inspect `errors` for `Stopped`, `Cancelled` or `Invalidated` jobs. A status response can be HTTP 200 even when the job has failed.

Download a returned file URL promptly. Do not forward your API token to another host when following a signed download URL. If the URL expires, submit the request again or retrieve a fresh job result.

## Read results carefully

- Preserve coordinates, valid times, output units, missing-value markers and any ensemble dimension.
- A percentile is not an ensemble member or a mean. Summing daily percentiles is not the percentile of a multi-day total.
- A rate (for example mm/h) must be integrated over its interval before comparing it with accumulated rainfall in mm.
- Do not combine fractional (0–1) and percentage (0–100) probabilities without conversion.
- An absent or null value is not zero. Check coverage before computing daily or regional summaries.

## Postman

[Download the collection](../assets/tngap_api.postman_collection.zip). Import it and set `gap_api_token`; the default examples use retained historical data. The collection also includes discovery, daily NextGen, cleaned daily precipitation, upload and job-status requests. Set forecast dates to an available run before executing forecast examples.

## Errors

| HTTP status | What to check |
|---|---|
| 400 | Invalid or inactive fields, wrong product/field pairing, date-range limit, location, output format, or mixed ensemble/non-ensemble CSV fields. |
| 401 / 403 | Missing or expired credentials, or no permission for the selected product. |
| 404 | No data for the query, an unavailable result, or a job not accessible to your account. |
| 410 | Retired product after the retirement release is deployed; see [product changes](product-changes.md). |
| 429 | Rate limit reached. Respect `Retry-After` when present and reduce request frequency. |
| 500 | Server-side processing failure. Retain the request, time and job ID for support; inspect job errors. |

Check the response status before opening a download as NetCDF or CSV. An error body is not a data file. Start with a small point/date query before expanding the request.
