class EIAApi:
    """EIAApi contains helper methods to fetch EIA data."""

    def __init__(self, client):
        self.client = client

    def emissions_by_state_by_fuel(self):
        """emissions_by_state_by_fuel returns a JSON list containing"""
        response = self.client.get(
            "/state-electricity-profiles/emissions-by-state-by-fuel/data"
        )
        raise "Not implemented yet."
        # structure the response ourselves in a nice to digest format
