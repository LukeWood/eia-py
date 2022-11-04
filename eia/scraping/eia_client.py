import requests


class EIAClient:
    """EIACLient contains methods to get data from the EIAApi.

    The primary purpose of this class is to provide a layer of abstraction around the
    HTTP calls required to get access to the EIA data.
    """

    def __init__(self, api_key):
        if not isinstance(api_key, str):
            raise ValueError(
                "Expected `api_key` to be a string.  Instead, got "
                f"api_key={api_key}."
            )
        self.api_key = api_key

    def request(self, route):
        """`request()` performs a get request to the specified route, returning JSON.

        `request()` performs a get request using the specified API key, and returns a
        dictionary representing the response JSON provided by the EIA api.

        Returns:
            dictionary containing response.
        """
        if route[0] != "/":
            raise ValueError("All routes must start with '/'.  Got " f"route={route}.")

        response = f"{self.base_url}{route}?api_key={self.api_key}"
        return response.json()

    def base_url(self):
        """base_url contains the base url for the EIA api"""
        return "https://api.eia.gov/v2/electricity"
