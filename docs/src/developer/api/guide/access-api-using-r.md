# R

Use `httr` to request a NetCDF file and `ncdf4` to inspect it. The example uses IMERG V07 daily satellite rainfall.

## Install and authenticate

```r
install.packages(c("httr", "ncdf4"))
```

Set `GAP_API_TOKEN` in your environment before starting R or RStudio. The sample reads `Sys.getenv("GAP_API_TOKEN")`; it does not contain a key. See [API keys](api-keys.md).

## Download and run

Download [sample.R](https://github.com/kartoza/tomorrownow_gap_documentation/blob/main/examples/sample.R) and run it in RStudio or with `Rscript sample.R`.

The request uses:

```r
params <- list(
  product = "imerg_v07",
  attributes = "precipitation",
  start_date = "2026-09-01", end_date = "2026-09-03",
  output_type = "netcdf", bbox = "36.7,-1.4,36.9,-1.2"
)
```

The script checks HTTP status, validates the NetCDF file, prints the variables and rainfall range, and saves `data.nc`. It closes the NetCDF handle and removes the temporary file even if processing fails.

## Multiple points

[Download sample_points.R](https://github.com/kartoza/tomorrownow_gap_documentation/blob/main/examples/sample_points.R). Provide `points.csv` with numeric `lon` and `lat` columns in WGS84 decimal degrees. It downloads one CSV per point and stops on an HTTP error. Reduce request frequency if the API responds with 429.

## Change products

Choose field identifiers from the [product reference](measurements/data-products.md). For a forecast, update the dates to an available run and valid period. NextGen daily rainfall uses names such as `precip_accum_p50`; historical CBAM uses a different field vocabulary.

Do not assume NetCDF dimension order. Inspect `nc$var` and coordinates before extracting or plotting a slice. Missing values are not zero. A forecast percentile is not the percentile of a sum across days.
