import os
import requests


class SheetWriter:

    def __init__(self):
        self.sheety_endpoint = "https://api.sheety.co/954119ebc378bd2f70a8a60b57fdd0d2/myWorkouts/workouts"
        self.sheety_params = {
            "workout": {
            }
        }
        self.headers = {
            "authorization": os.environ.get("SHEETY_TOKEN")
        }

    def write(self):
        response = requests.post(self.sheety_endpoint, json=self.sheety_params, headers=self.headers)
        response.raise_for_status()
