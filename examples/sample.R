# Download retained historical data. Set GAP_API_TOKEN before running.
library(httr)
library(ncdf4)

token <- Sys.getenv("GAP_API_TOKEN")
if (!nzchar(token)) stop("Set GAP_API_TOKEN to your GAP API key")
params <- list(
  product = "imerg_v07",
  attributes = "precipitation",
  start_date = "2026-09-01", end_date = "2026-09-03",
  output_type = "netcdf", bbox = "36.7,-1.4,36.9,-1.2"
)
output <- "data.nc"
temporary <- tempfile(fileext = ".nc")
tryCatch({
  response <- GET(
    "https://gap.tomorrownow.org/api/v1/measurement/",
    add_headers(Authorization = paste("Token", token)),
    query = params, timeout(300), write_disk(temporary, overwrite = TRUE)
  )
  stop_for_status(response)
  content_type <- headers(response)[["content-type"]]
  if (!is.null(content_type) && grepl("json|text/html", content_type)) {
    stop("Expected NetCDF; received JSON or HTML")
  }
  nc <- nc_open(temporary)
  tryCatch({
    print(nc)
    print(names(nc$var))
    rainfall <- ncvar_get(nc, "precipitation")
    print(range(rainfall, na.rm = TRUE))
  }, finally = nc_close(nc))
  if (!file.copy(temporary, output, overwrite = TRUE)) stop("Could not save output")
  cat("Saved", output, "\n")
}, finally = unlink(temporary))
