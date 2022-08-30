import requests
import os


NUTRITIONIX_KEY = os.environ.get("NUTRITIONIX_KEY")
NUTRITIONIX_ID = os.environ.get("NUTRITIONIX_ID")
GENDER = "Male"
WEIGHT_KG = 68
HEIGHT_CM = 178
AGE = 18


class Exercise:

    def __init__(self):
        self.nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
        self.exercise = self.get_exercise()
        self.response = None
        self.headers = {
            "x-app-id": NUTRITIONIX_ID,
            "x-app-key": NUTRITIONIX_KEY,
        }
        self.exercise_params = {
            "query": self.exercise,
            "gender": GENDER,
            "weight_kg": WEIGHT_KG,
            "height_cm": HEIGHT_CM,
            "age": AGE,
        }

    def get_exercise(self):
        self.exercise = input("What exercises have you done today? ")
        return self.exercise

    def process_exercise(self):
        self.response = requests.post(self.nutritionix_endpoint, headers=self.headers, json=self.exercise_params)
        self.response.raise_for_status()
        exercise_data = self.response.json()["exercises"]
        return exercise_data
