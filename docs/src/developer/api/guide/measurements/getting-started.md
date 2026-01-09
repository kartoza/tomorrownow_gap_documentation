---
title: Getting Started
summary: Authentication and basic API usage
  - Irwan Fathurrahman
date: 2024-06-18
some_url: https://github.com/kartoza/tomorrownow_gap.git
copyright: Copyright 2024, Kartoza
contact:
license: This program is free software; you can redistribute it and/or modify it under the terms of the GNU Affero General Public License as published by the Free Software Foundation; either version 3 of the License, or (at your option) any later version.
---

# Getting Started with the API

In order to use the API, the user must be authenticated and must have authorisation to access the data.

Let's see how to use the API and what sequence of API calls can lead us to get data for analysis.

Once you open the above link the Swagger will open. Click on the 1️⃣ `Authorize` button, to open the authorisation form.

![Authorise](../img/api-guide-1.png)

To authorize, please enter your `Username` and `Password` Once you have entered your credentials, click the `Authorize` button to complete the authorisation process.

![Authorise form](../img/api-guide-2.png)

Click on the close button or cross button to close the authorisation form.

![Close](../img/api-guide-3.png)

**Examples of Usage of the OSIRIS II API**

Please note that the data in the examples provided below DO NOT reflect the actual data in TomorrowNow.

## Accessing the OSIRIS II API

To use the API click on the Weather & Climate Data 1️⃣.

![Measurement API](../img/api-guide-4.png)

**Weather & Climate Data API:**

Click on the GET API it will show the parameters to enter to get the data. Click on the 1️⃣ `Try it out` button, to fill the detailed in the 2️⃣ available request parameters. After filling the details click on the 3️⃣ `Execute` button, to run the API.

![GET API](../img/api-guide-5.png)
![GET API](../img/api-guide-6.png)

**Example of response:**

![GET API RESPONSE](../img/api-guide-7.png)

**Available format types**

### JSON

This type is only available for querying by single point.
![JSON](../img/api-guide-7.png)

###  CSV

The user can download the file to check the response
![CSV](../img/api-guide-12.png)

### NETCDF

The user can download the file to check the response
![netcdf](../img/api-guide-13.png)

To read/write the netcdf file user can refer to below link
https://docs.xarray.dev/en/stable/user-guide/io.html#netcdf
