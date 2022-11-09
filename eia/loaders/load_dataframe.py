import os

import pandas as pd

import eia

mapping = {
    "electric-power-operational-data": "electric-power-operational-data_data.csv",
    "facility-fuel": "facility-fuel_data.csv",
    "operating-generator-capacity": "operating-generator-capacity_data.csv",
    "retail-sales": "retail-sales_data.csv",
}


def load_dataframe(data, download_data=None, data_dir=None):
    """Loads the eia data into a `pd.DataFrame`

    Args:
        data: string, required.  Must be one of 'electric-power-operational-data',
            'facility-fuel', 'operating-generator-capacity', 'retail-sales'.
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
    path = f"{data_dir}/data/csv/{path}"
    print(path)
    if download_data:
        eia.scraping.download_data(data_dir=data_dir)
    if download_data is None and not os.path.exists(path):
        eia.scraping.download_data(data_dir=data_dir)

    return pd.read_csv(path)
