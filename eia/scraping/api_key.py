import os


def api_key():
    """Returns the eia api key from the os.environment variable.

    Returns:
        the value of your OS's 'EIA_API_KEY' environment variable.
    Raises:
        AssertionError if api key is not set.
    """
    api_key = os.environ.get("EIA_API_KEY", None)
    assert api_key is not None
    return api_key
