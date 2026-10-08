# points.csv must contain numeric lon and lat columns in WGS84 degrees.
library(httr)
token <- Sys.getenv("GAP_API_TOKEN")
if (!nzchar(token)) stop("Set GAP_API_TOKEN to your GAP API key")
points <- read.csv("points.csv")
stopifnot(all(c("lon", "lat") %in% names(points)))
stopifnot(is.numeric(points$lon), is.numeric(points$lat))
stopifnot(all(is.finite(points$lon)), all(is.finite(points$lat)))
stopifnot(all(abs(points$lon) <= 180), all(abs(points$lat) <= 90))
for (i in seq_len(nrow(points))) {
  params <- list(
    product = "imerg_v07",
    attributes = "precipitation",
    start_date = "2026-09-01", end_date = "2026-09-03",
    output_type = "csv", lon = points$lon[i], lat = points$lat[i]
  )
  temporary <- tempfile(fileext = ".csv")
  tryCatch({
    response <- GET(
      "https://gap.tomorrownow.org/api/v1/measurement/",
      add_headers(Authorization = paste("Token", token)),
      query = params, timeout(300), write_disk(temporary, overwrite = TRUE)
    )
    stop_for_status(response)
    content_type <- headers(response)[["content-type"]]
    if (!is.null(content_type) && grepl("json|text/html", content_type)) {
      stop("Expected CSV; received JSON or HTML")
    }
    if (!file.copy(temporary, sprintf("point_%d.csv", i), overwrite = TRUE)) {
      stop("Could not save output")
    }
  }, finally = unlink(temporary))
  Sys.sleep(1)
}
