# Forecast availability

Model run time, provider publication time, GAP ingestion time and data availability are different events. A fixed clock-time schedule does not prove that a particular run is ready. Use available valid times and returned metadata when selecting a forecast.

## Nominal horizons

| Product | Catalogue horizon / time support |
|---|---|
| NextGen daily, including Nigeria | 10-day forecast, daily values |
| NextGen hourly, including Nigeria | 4-day forecast, hourly values |
| Google WeatherNext 2 | 15-day forecast; six-hour rainfall intervals |
| Daily precipitation forecast | 14-day daily rainfall statistics |
| Kenya rainfall forecast | 42-day daily rainfall |
| NeuralGCM S2S | Historical catalogue labelled 2021–2025 and a separate realtime product; inspect available times |

These labels are not guarantees of complete date or spatial coverage. The public options endpoint lists fields, not completed ingestion runs, and does not report freshness.

## Choosing a run

1. Check the [live catalogue](https://gap.tomorrownow.org/api/v1/docs/) and account access.
2. Request a small point and date range within the forecast horizon.
3. Where forecast archives are supported, set `forecast_date` explicitly. The API accepts a date or hourly initialisation such as `YYYY-MM-DDTHH`; support depends on the reader and archive.
4. Inspect the returned dates and metadata and retain the original request with your analysis.
5. If there is no data, distinguish an unavailable run, out-of-coverage location, delayed ingestion and missing measurements. Do not substitute zero.

When comparing forecasts, align both their valid times and lead times. Do not apply the old GenCast/GraphCast timestamp adjustments to WeatherNext 2.

For a confirmed publication schedule or archive-retention window, contact the GAP service administrator with the product and requested run. This guide does not publish unverified ingestion completion times.
