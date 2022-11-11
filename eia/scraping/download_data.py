##### Important TODOS:
# - refactor download_data for code quality
# - manage paths better

import json
import os
import re

import pandas as pd
import requests
import tqdm

import eia


def download_data(data_dir=None):
    """downloads the dataset to the specified `data_dir`.

    This should be run once to scrape the entire dataset.
    Can be re-run if you want to refresh your dataset.

    Args:
        data_dir: (optional) path to save the output data to.
    """
    print("Downloading data...")
    data_dir = data_dir or eia.utils.get_base_dir()
    api_key = eia.scraping.api_key()

    base_url = "https://api.eia.gov/v2/electricity/?api_key="
    api_base_url = "https://api.eia.gov/v2/electricity/"
    response = get_response(base_url, api_key)

    print("Scraping route schemas...")
    for i in tqdm.tqdm(response["response"]["routes"]):
        resp_schema = get_response(
            "".join([api_base_url, "/", i["id"], "?api_key="]), api_key
        )
        base_str = "".join([api_base_url, "/", i["id"], "/data?api_key=", api_key])

        schema_path = os.path.join(data_dir, "schema")
        eia.utils.ensure_exists(schema_path)

        file_path = os.path.join(schema_path, i["id"] + "_schema")
        with open(file_path, "w") as f:
            f.write(json.dumps(resp_schema, indent=2))

        data_path = os.path.join(data_dir, "data")
        eia.utils.ensure_exists(data_path)
        eia.utils.ensure_exists(f"{data_path}/json")
        eia.utils.ensure_exists(f"{data_path}/csv")

        if i["id"] != "state-electricity-profiles" and i["id"] != "rto":

            for j in resp_schema["response"]["data"]:
                base_str = "".join([base_str, "&data[]=", j])
            base_str = "".join(
                [base_str, "&end=", resp_schema["response"]["endPeriod"]]
            )
            resp = get_response(base_str)
            json_file_path = os.path.join(data_dir, "data", "json", i["id"] + "_data")
            csv_file_path = os.path.join(data_dir, "data", "csv", i["id"] + "_data")
            with open(json_file_path, "w") as f:
                f.write(json.dumps(resp["response"], indent=2))
                df = pd.json_normalize(resp["response"]["data"])
                df.to_csv("".join([csv_file_path, ".csv"]))

    for k in ["rto", "state-electricity-profiles"]:

        base_url = f"https://api.eia.gov/v2/electricity/{k}?api_key="
        api_base_url = f"https://api.eia.gov/v2/electricity/{k}"
        response = get_response(base_url, api_key)

        print(f"Scraping {k} data...")
        for i in tqdm.tqdm(response["response"]["routes"]):
            resp_schema = get_response(
                "".join([api_base_url, "/", i["id"], "?api_key="]), api_key
            )

            base_str = "".join([api_base_url, "/", i["id"], "/data?api_key=", api_key])
            eia.utils.ensure_exists(f"{data_dir}/schema/{k}")
            eia.utils.ensure_exists(f"{data_dir}/data/{k}/json")
            eia.utils.ensure_exists(f"{data_dir}/data/{k}/csv")

            file_path = os.path.join(data_dir, "schema", k, i["id"] + "_schema")
            with open(file_path, "w") as f:
                f.write(json.dumps(resp_schema["response"], indent=2))

            for j in resp_schema["response"]["data"]:
                base_str = "".join([base_str, "&data[]=", j])
            base_str = "".join(
                [
                    base_str,
                    "&end=",
                    str(resp_schema["response"]["endPeriod"]),
                    "&sort[0][column]=period&sort[0][direction]=desc",
                ]
            )

            resp = get_response(base_str)
            json_file_path = os.path.join(
                data_dir, "data", k, "json", i["id"] + "_data"
            )
            csv_file_path = os.path.join(data_dir, "data", k, "csv", i["id"] + "_data")

            with open(json_file_path, "w") as f:
                f.write(json.dumps(resp["response"], indent=2))
                df = pd.json_normalize(resp["response"]["data"])
                df.to_csv("".join([csv_file_path, ".csv"]))
            max_val = resp["response"]["total"]
            if max_val > 50000:
                max_val = 50000
            base_str = "".join([base_str, "&offset=", str(0)])
            for offset_val in range(5000, max_val, 5000):
                base_str = re.sub(
                    "&offset=[0-9]*", "&offset=" + str(offset_val), base_str
                )
                resp = get_response(base_str)
                json_file_path = os.path.join(
                    data_dir, "data", k, "json", i["id"] + "_data"
                )
                csv_file_path = os.path.join(
                    data_dir, "data", k, "csv", i["id"] + "_data"
                )

                with open(json_file_path, "a") as f:
                    f.write(json.dumps(resp["response"], indent=2))
                    df = pd.json_normalize(resp["response"]["data"])
                    df.to_csv("".join([csv_file_path, ".csv"]), mode="a")


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
