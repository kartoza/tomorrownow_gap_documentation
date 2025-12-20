# GAP Ingestor Schedule

Below is the ingestor schedule of datasets in GAP.


| Dataset | Frequency | Model Run (UTC) | Model Available (UTC) | GAP Start Time (UTC) | GAP End Time (UTC) | Available Time (UTC) | Retention Policy |
|-------|-----------|-----------------|------------------------|---------------------|-------------------|----------------------|------------------|
| CBAM Daily Short-Term Forecast 00Z | Once per day | 00:00:00 | – | 00:10:00 | 02:13:00 | 02:23:00 | Stored in the latest and historical Zarr |
| CBAM Daily Short-Term Forecast 06Z | Twice per day | 06:00:00 | – | 08:30:00 | 09:20:00 | 09:40:00 | – |
| CBAM Hourly Short-Term Forecast | Once per day | – | – | 00:30:00 | 06:03:00 | 06:43:00 | Stored in the latest Zarr only (no historical archive) |
| Google GenCast | Once per day | 00:00:00 | 08:05:00 | 09:05:00 | 09:43 | 10:00 | Stored in the latest and historical Zarr |
| Google GraphCast | Once per day | 18:00:00 | 00:45:00 | 02:00:00 | 02:30:00 | 02:35:00 | Stored in the latest and historical Zarr |
| Google Nowcast | Four times per day (every 6 hours at :15 UTC) | – | – | 00:15:00<br>06:15:00<br>12:15:00<br>18:15:00 | 00:45:00<br>06:45:00<br>12:45:00<br>18:45:00 | 02:25:00<br>07:00:00<br>13:00:00<br>19:00:00 | 00:00 and 12:00 models stored in the historical Zarr |
| Salient | Once per week (every Monday) | – | – | 04:00:00 | 04:52:00 | 05:58:00 | Stored in the latest and historical Zarr |
| Salient GEMV2 | Once per week (every Monday) | – | – | 10:00:00 | 10:05:00 | 10:55:00 | Stored in the latest and historical Zarr |
