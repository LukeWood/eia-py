"""
TODOs:
    - Document the script
    - Improve Code Quality
"""

import json
import os

import pandas as pd
import requests

import eia


def get_response(base_url, api_key=""):
    """
    Returns the JSON response of the API

    Returns:
        The JSON response of the API

    Raises:
        AssertionError if base_url is not available.

    """

    assert base_url != ""
    if api_key != "":
        return requests.get("".join([base_url, api_key])).json()
    return requests.get(base_url).json()


api_key = eia.scraping.api_key()

base_url = "https://api.eia.gov/v2/electricity/?api_key="
api_base_url = "https://api.eia.gov/v2/electricity/"
response = get_response(base_url, api_key)

for i in response["response"]["routes"]:

    resp_schema = get_response(
        "".join([api_base_url, "/", i["id"], "?api_key="]), api_key
    )
    base_str = "".join([api_base_url, "/", i["id"], "/data?api_key=", api_key])
    file_path = os.path.join(
        os.getcwd(), "eia", "scraping", "Schema", i["id"] + "_schema"
    )
    with open(file_path, "w") as f:
        f.write(json.dumps(resp_schema, indent=2))

    if i["id"] != "state-electricity-profiles" and i["id"] != "rto":

        for j in resp_schema["response"]["data"]:
            base_str += "&data[]=" + j
        resp = get_response(base_str)
        json_file_path = os.path.join(
            os.getcwd(), "eia", "scraping", "Data", "json", i["id"] + "_data"
        )
        csv_file_path = os.path.join(
            os.getcwd(), "eia", "scraping", "Data", "csv", i["id"] + "_data"
        )
        with open(json_file_path, "w") as f:
            f.write(json.dumps(resp["response"], indent=2))
            df = pd.json_normalize(resp["response"]["data"])
            df.to_csv("".join([csv_file_path, ".csv"]))

for k in ["rto", "state-electricity-profiles"]:

    base_url = f"https://api.eia.gov/v2/electricity/{k}?api_key="
    api_base_url = f"https://api.eia.gov/v2/electricity/{k}"
    response = get_response(base_url, api_key)

    for i in response["response"]["routes"]:
        resp_schema = get_response(
            "".join([api_base_url, "/", i["id"], "?api_key="]), api_key
        )

        base_str = "".join([api_base_url, "/", i["id"], "/data?api_key=", api_key])

        file_path = os.path.join(
            os.getcwd(), "eia", "scraping", "Schema", k, i["id"] + "_schema"
        )
        with open(file_path, "w") as f:
            f.write(json.dumps(resp_schema["response"], indent=2))

        for j in resp_schema["response"]["data"]:
            base_str = "".join([base_str, "&data[]=", j])

        resp = get_response(base_str)
        json_file_path = os.path.join(
            os.getcwd(), "eia", "scraping", "Data", k, "json", i["id"] + "_data"
        )
        csv_file_path = os.path.join(
            os.getcwd(), "eia", "scraping", "Data", k, "csv", i["id"] + "_data"
        )

        with open(json_file_path, "w") as f:
            f.write(json.dumps(resp["response"], indent=2))
            df = pd.json_normalize(resp["response"]["data"])
            df.to_csv("".join([csv_file_path, ".csv"]))
