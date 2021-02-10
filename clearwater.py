import requests


class Clearwater:
    def __init__(self):
        self.host = 'https://www.clearwatertrackingsystem.com/api/v1'
        self.api_key = your_api_key
        self.headers = {'Accept': 'application/json'}

    def get_all_vessels(self):
        url = f'{self.host}/vessel?api_key={self.api_key}'
        response = requests.get(url, self.headers)

        if response.status_code != 200:
            return print('Error: '+response.json().get('message'))
        return response.json()

    def get_vessel_by_imo(self, imo: int):
        for vessel in self.get_all_vessels():
            if vessel.get('imo') == imo:
                return vessel
        else:
            return 'Vessel not found'

    def get_vessel_by_clearwater_id(self, clearwater_id: int):
        url = f'{self.host}/vessel/{clearwater_id}?api_key={self.api_key}'
        response = requests.get(url, self.headers)

        if response.status_code != 200:
            return print('Error: '+response.json().get('message'))
        return response.json()

    def get_all_alerts(self):
        url = f'{self.host}/alert?api_key={self.api_key}'
        response = requests.get(url, self.headers)

        if response.status_code != 200:
            return print('Error: '+response.json().get('message'))
        return response.json()

    def get_specific_alert(self, alert_id):
        url = f'{self.host}/alert/{alert_id}?api_key={self.api_key}'
        response = requests.get(url, self.headers)

        if response.status_code != 200:
            return print('Error: '+response.json().get('message'))
        return response.json()
