# Spreadsheet Link: https://docs.google.com/spreadsheets/d/1tYcoPfOz-dAqxaBA822cgDOtBvP0vDIayvuxKWTbTxw/edit?usp=sharing

from exercise import Exercise
from sheets_writer import SheetWriter
from datetime import datetime

exercise = Exercise()
writer = SheetWriter()

now = datetime.now()
date = now.strftime("%d/%m/%Y")
time = now.strftime("%H:%M:%S")

exercise_data = exercise.process_exercise()
for exercise in exercise_data:
    writer.sheety_params = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }
    writer.write()
