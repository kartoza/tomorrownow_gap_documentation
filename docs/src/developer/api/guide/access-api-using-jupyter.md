# Python and Jupyter Notebook

Download a NetCDF subset of IMERG V07 daily satellite rainfall, then inspect it with xarray. This example uses a small bounding box and fixed historical dates. For a forecast, change the product, fields and dates together using the [catalogue](measurements/data-products.md).

## Install and authenticate

```bash
pip install requests xarray netCDF4 notebook
export GAP_API_TOKEN='YOUR_API_KEY'
```

Create a key using the [API key guide](api-keys.md). Launch Jupyter from the same environment so the notebook can read `GAP_API_TOKEN`.

## Run the example

Download [sample.py](https://github.com/kartoza/tomorrownow_gap_documentation/blob/main/examples/sample.py) or [sample.ipynb](https://github.com/kartoza/tomorrownow_gap_documentation/blob/main/examples/sample.ipynb). Run `python sample.py`, or open the notebook with `jupyter notebook` and run its cell.

The script:

1. Requests `precipitation` from `imerg_v07` for 1–3 September 2026.
2. Downloads into a temporary file and checks the HTTP status before replacing `data.nc`.
3. Opens the completed file with xarray and prints coordinates, units and variables.

Errors raise an exception. If a request fails, an older `data.nc` is not reopened as though it were a new result.

## Change the request

```python
params = {
    "product": "imerg_v07",
    "attributes": "precipitation",
    "start_date": "2026-09-01",
    "end_date": "2026-09-03",
    "output_type": "netcdf",
    "bbox": "36.7,-1.4,36.9,-1.2",
}
```

A bounding box is west, south, east, north. For a point, remove `bbox` and supply both `lat` and `lon`. JSON supports a single point; adapt the response handling to call `response.json()` rather than saving it as NetCDF.

For NextGen daily forecasts, use `nextgen_forecast` with fields such as `precip_accum_p50,precip_accum_p75,tmin_c,tmax_c` and available forecast dates. Read [run selection](measurements/ingestor-schedule.md) before pinning `forecast_date`.

## Inspect the data

```python
import xarray as xr

with xr.open_dataset("data.nc") as dataset:
    print(dataset)
    print(dataset["precipitation"].attrs)
    print(dataset.coords)
```

Dimension names and shapes depend on the product; do not assume a fixed grid. Preserve missing values. For long requests use [background jobs](measurements/advanced-usage.md#submit-a-background-request).
