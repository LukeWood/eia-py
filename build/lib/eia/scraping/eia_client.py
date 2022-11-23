import requests


class EIAClient:
    """EIACLient contains methods to get data from the EIAApi.

    The primary purpose of this class is to provide a layer of abstraction around the
    HTTP calls required to get access to the EIA data.


    Usage:

    ```python
    import eia

    client = eia.scraping.EIAClient(api_key=eia.scraping.api_key())
    client.get('/v2/electricity/retail-sales/')
    ```
    """

    def __init__(self, api_key):
        if not isinstance(api_key, str):
            raise ValueError(
                "Expected `api_key` to be a string.  Instead, got "
                f"api_key={api_key}."
            )
        self.api_key = api_key

    def get(self, route):
        """`get()` performs a get request to the specified route, returning JSON.

        `get()` performs a get request using the specified API key, and returns a
        dictionary representing the response JSON provided by the EIA api.

        Returns:
            dictionary containing response.
        """
        if route[0] != "/":
            raise ValueError(f"All routes must start with '/'.  Got route={route}.")

        path = f"{self.base_url}{route}?api_key={self.api_key}"
        response = requests.get(path)
        return response.json()

    @property
    def base_url(self):
        """base_url contains the base url for the EIA api"""
        return "https://api.eia.gov/v2/electricity"
