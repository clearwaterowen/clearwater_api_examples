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

    def get_specific_vessel(self, vessel_id):
        url = f'{self.host}/vessel/{vessel_id}?api_key={self.api_key}'
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
