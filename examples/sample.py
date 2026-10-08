"""Download retained GAP historical data; set GAP_API_TOKEN before running."""

import os
from pathlib import Path

import requests

API_URL = "https://gap.tomorrownow.org/api/v1/measurement/"
PARAMS = {
    "product": "imerg_v07",
    "attributes": "precipitation",
    "start_date": "2026-09-01",
    "end_date": "2026-09-03",
    "output_type": "netcdf",
    "bbox": "36.7,-1.4,36.9,-1.2",
}


def download_file(params, output="data.nc", token=None):
    """Download a synchronous result, replacing output only after success."""
    token = token or os.environ.get("GAP_API_TOKEN")
    if not token:
        raise ValueError("Set GAP_API_TOKEN to your GAP API key")
    target = Path(output)
    temporary = target.with_suffix(target.suffix + ".part")
    try:
        with requests.get(
            API_URL,
            params=params,
            headers={"Authorization": f"Token {token}"},
            stream=True,
            timeout=(15, 300),
        ) as response:
            response.raise_for_status()
            content_type = response.headers.get("Content-Type", "").lower()
            if "json" in content_type or "text/html" in content_type:
                raise ValueError("Expected a data file; received JSON or HTML")
            with temporary.open("wb") as stream:
                for chunk in response.iter_content(chunk_size=65536):
                    stream.write(chunk)
        temporary.replace(target)
    finally:
        temporary.unlink(missing_ok=True)
    return target


if __name__ == "__main__":
    import xarray as xr

    path = download_file(PARAMS)
    with xr.open_dataset(path) as dataset:
        print(dataset)
        print(dataset["precipitation"])
