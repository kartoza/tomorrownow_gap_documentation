---
title: Advanced Usage
summary: Code examples, location upload, and API reference
  - Irwan Fathurrahman
date: 2024-06-18
some_url: https://github.com/kartoza/tomorrownow_gap.git
copyright: Copyright 2024, Kartoza
contact:
license: This program is free software; you can redistribute it and/or modify it under the terms of the GNU Affero General Public License as published by the Free Software Foundation; either version 3 of the License, or (at your option) any later version.
---

# Advanced Usage

**Example of codes to access the API**

## Python

```python
import requests
from requests.auth import HTTPBasicAuth

url = "https://gap.tomorrownow.org/api/v1/measurement/?lat=-1.404244&lon=35.008688&attributes=max_temperature,min_temperature&start_date=2019-11-01&end_date=2019-11-02&product=cbam_historical_analysis&output_type=json"

payload={}

# --- Option 1: Using username and password ---
headers = {}
basic = HTTPBasicAuth('YOUR_USERNAME', 'YOUR_PASSWORD')
response = requests.get(url, auth=basic, data=payload)
print(response.json())

# --- Option 2: Using API Token ---
token = "YOUR_API_TOKEN"
headers = {'Authorization': f'Token {token}'}
response = requests.get(url, headers=headers, data=payload)
print(response.json())
```

## CURL

```
# --- Option 1: Using username and password ---
curl --location 'https://gap.tomorrownow.org/api/v1/measurement/?lat=-1.404244&lon=35.008688&attributes=max_temperature%2Cmin_temperature&start_date=2019-11-01&end_date=2019-11-02&product=cbam_historical_analysis&output_type=json' \
-u 'YOUR_USERNAME:YOUR_PASSWORD'

# --- Option 2: Using API Token ---
curl --location 'https://gap.tomorrownow.org/api/v1/measurement/?lat=-1.404244&lon=35.008688&attributes=max_temperature%2Cmin_temperature&start_date=2019-11-01&end_date=2019-11-02&product=cbam_historical_analysis&output_type=json' \
--header 'Authorization: Token YOUR_API_TOKEN'
```

## JavaScript-JQuery

```js
var url = "https://gap.tomorrownow.org/api/v1/measurement/?lat=-1.404244&lon=35.008688&attributes=max_temperature,min_temperature&start_date=2019-11-01&end_date=2019-11-02&product=cbam_historical_analysis&output_type=json";

// --- Option 1: Using username and password (Basic Auth) ---
var basicAuth = "Basic " + btoa("YOUR_USERNAME:YOUR_PASSWORD");

$.ajax({
  url: url,
  method: "GET",
  timeout: 0,
  headers: {
    "Authorization": basicAuth
  },
}).done(function (response) {
  console.log(response);
});

// --- Option 2: Using API Token ---
$.ajax({
  url: url,
  method: "GET",
  timeout: 0,
  headers: {
    "Authorization": "Token YOUR_API_TOKEN"
  },
}).done(function (response) {
  console.log(response);
});
```


## Upload Location API

Using the Location API, you can upload the geometry to query the data by polygon or list of point. You can upload the geometry in one of format: geojson/shapefile/gpkg. The file must be in WGS84 or CRS 4326. The uploaded location will have expiry date time (2 months). Once the server removes your geometry after the expiry time, you need to reupload your geometry.

Note: when using shapefile, the .shp, .dbf, .shx files must be in the zip root directory.


Click on the 1️⃣ Upload Location POST API to view the usage option. Click on the 2️⃣ `Try it out` button, to enable the fields to enter the attributes.

![POST API](../img/api-guide-9.png)

Fill the location_name and select your file to upload in the 1️⃣ available fields. After filling the details click on the 2️⃣ `Execute` button, to run the API.

![POST API](../img/api-guide-10.png)

**Example of response:**

![POST API RESPONSE](../img/api-guide-11.png)

You can see the expiry date time for your geometry in the `expired_on` field.

## API Postman Collection

You can download the postman collection below and import the API collection using your postman. Once imported, you need to set the variable `gap_api_username` and `gap_api_password` using your credentials.

[Download](../assets/tngap_api.postman_collection.zip)


## Error codes

| Response code | Message | Reason |
|---------------|---------|--------|
| 400 | Unknown geometry type! | Use geometry with type Polygon/Multipolygon/MultiPoint to make a request using POST method |
| 400 | Output format json is only available for single point query! | JSON output is only available for GET method with singe point query. Please use csv/netcdf output format! |
| 400 | No matching attribute found! | The attribute list cannot be found in the product type. |
| 400 | Attribute with ensemble cannot be mixed with non-ensemble | When requesting for product type salient_seasonal_forecast and output is csv, the attribute that is in ensemble (50-values) cannot be requested with the attribute that does not have ensemble. Please use netcdf output format instead! |
| 400 | Incorrect output type | Use either json, csv, netcdf or ascii |
| 404 | No weather data is found for given queries | |
| 429 | Too many requests | You have hit the rate limit |
