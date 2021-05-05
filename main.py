import requests
from datetime import datetime
from secret import Application_ID, Application_Keys, Authorization_token

api_origen = "https://trackapi.nutritionix.com"
search = "/v2/natural/exercise"
search_path = f"{api_origen}{search}"
exercise_text = input("Tell me which exercises you did: ")
header = {
    "x-app-id": Application_ID,
    "x-app-key": Application_Keys
}
params = {
    "query": exercise_text,
    "gender": "male",
    "weight_kg": 88.5,
    "height_cm": 184.64,
    "age": 36
}
response = requests.post(url=search_path, headers=header, json=params)
result = response.json()
today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")
sheets_get_path = "https://api.sheety.co/32c894fc5869b0d61487c00f3b006cb5/myWorkouts/workouts"
sheets_post_path = "https://api.sheety.co/32c894fc5869b0d61487c00f3b006cb5/myWorkouts/workouts"
header_sheet = {
    "Authorization": Authorization_token
}
for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    response = requests.post(url=sheets_post_path, headers=header_sheet, json=sheet_inputs)
print("Thanks your tracking was saved ")
