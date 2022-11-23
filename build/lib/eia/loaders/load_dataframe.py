import os

import pandas as pd

import eia

mapping = {
    "electric-power-operational-data": "csv/electric-power-operational-data_data.csv",
    "facility-fuel": "csv/facility-fuel_data.csv",
    "operating-generator-capacity": "csv/operating-generator-capacity_data.csv",
    "retail-sales": "csv/retail-sales_data.csv",
    "rto-daily-fuel-type-data": "rto/csv/daily-fuel-type-data_data.csv",
    "rto-daily-interchange-data": "rto/csv/daily-interchange-data_data.csv",
    "rto-daily-region-data": "rto/csv/daily-region-data_data.csv",
    "rto-daily-region-sub-ba-data": "rto/csv/daily-region-sub-ba-data_data.csv",
    "rto-fuel-type-data": "rto/csv/fuel-type-data_data.csv",
    "rto-interchange-data": "rto/csv/interchange-data_data.csv",
    "rto-region-data": "rto/csv/region-data_data.csv",
    "rto-region-sub-ba-data": "rto/csv/region-sub-ba-data_data.csv",
    "state-electricity-profiles-capability": "state-electricity-profiles/csv/capability_data.csv",
    "state-electricity-profiles-emissions-by-state-by-fuel": "state-electricity-profiles/csv/emissions-by-state-by-fuel_data.csv",
    "state-electricity-profiles-meters": "state-electricity-profiles/csv/meters_data.csv",
    "state-electricity-profiles-net-metering": "state-electricity-profiles/csv/net-metering_data.csv",
    "state-electricity-profiles-source-disposition": "state-electricity-profiles/csv/source-disposition_data.csv",
    "state-electricity-profiles-summary": "state-electricity-profiles/csv/summary_data.csv",
}


def load_dataframe(data, download_data=None, data_dir=None):
    """Loads the eia data into a `pd.DataFrame`

    Args:
        data: string, required.  Must be one of 'electric-power-operational-data','facility-fuel', 'operating-generator-capacity', 'retail-sales', 'rto-daily-fuel-type-data', 'rto-daily-interchange-data', 'rto-daily-region-data','rto-daily-region-sub-ba-data', 'rto-fuel-type-data','rto-interchange-data','rto-region-data', 'rto-region-sub-ba-data', 'state-electricity-profiles-capability', 'state-electricity-profiles-emissions-by-state-by-fuel', 'state-electricity-profiles-meters', 'state-electricity-profiles-net-metering', 'state-electricity-profiles-source-disposition','state-electricity-profiles-summary'
        download_data: (Optional) boolean or None.  If None, downloads the data if the
            target CSV file does not exist.  If True, always downloads the file.  If
            False, never download the data.
        data_dir: (Optional) string base directory to store the data in.
    """
    if data not in mapping.keys():
        raise ValueError(
            f"Expected `data` to be one of {mapping.keys()}.  got " f"data={data}."
        )
    assert data in mapping.keys()
    assert download_data in [True, False, None]
    assert isinstance(data_dir, str) or data_dir is None
    data_dir = data_dir or eia.utils.get_base_dir()
    path = mapping[data]
    path = f"{data_dir}/data/{path}"
    if download_data:
        eia.scraping.download_data(data_dir=data_dir)
    if download_data is None and not os.path.exists(path):
        eia.scraping.download_data(data_dir=data_dir)

    return pd.read_csv(path)
