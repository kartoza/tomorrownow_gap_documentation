# Measurements API

The measurement API returns selected fields for a location and date range. Use one product per request and choose fields from that product's [reference](attributes-reference.md).

Base URL: `https://gap.tomorrownow.org/api/v1/`.

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `measurement/options/` | Discover product identifiers and their available attribute names. |
| GET | `measurement/` | Retrieve measurements or submit an asynchronous request. |
| GET | `measurement/job-status/{job_id}/` | Check your job and retrieve its result or download URL. |
| POST | `location/?location_name=NAME` | Upload a geometry file for later measurement requests. |
| GET | `consensus_blending/` | Request the daily precipitation layer with fixed fields `precipitation` and `primary`. |

Measurements use **GET**. Geometry uploads use **POST**. A product appearing in discovery does not guarantee your account has permission to read it.

## Output formats

| `output_type` | Use |
|---|---|
| `json` | A single latitude/longitude point; inspect metadata and data in the response. |
| `csv` | Tabular downloads. Do not mix ensemble and non-ensemble attributes in one CSV request. |
| `netcdf` | Grids, areas and ensemble data. Not supported for upper-air radiosonde observations. |
| `ascii` | Supported for compatible readers; check the interactive API and start with a small request. |

Use NetCDF when preserving coordinates and ensemble dimensions matters. Read the returned metadata rather than assuming all fields share a unit, scale or time interval. Missing values do not mean zero rainfall.

[Get started](getting-started.md) · [Choose a product](data-products.md)
