import requests
from datetime import datetime
import pandas
import matplotlib.pyplot as plt
import numpy as np

GENDER = "male"
WEIGHT_KG = 75
HEIGHT_CM = 175
AGE = 22

APP_ID = "00acd522"
API_KEY = "3bff7b1e9792e10ffdd50734f20f3f84"

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = "https://api.sheety.co/e36eb7699ce0fe41e2321b3f8aed327e/copyOfMyWorkouts/workouts"

exercise_text = input("Tell me which exercises you did: ")

# headers = {
#     "x-app-id": APP_ID,
#     "x-app-key": API_KEY,
# }

# parameters = {
#     "query": exercise_text,
#     "gender": GENDER,
#     "weight_kg": WEIGHT_KG,
#     "height_cm": HEIGHT_CM,
#     "age": AGE
# }

# response = requests.post(exercise_endpoint, json=parameters, headers=headers)
# result = response.json()



# today_date = datetime.now().strftime("%d/%m/%Y")
# now_time = datetime.now().strftime("%X")

# for exercise in result["exercises"]:
#     sheet_inputs = {
#         "workout": {
#             "date": today_date,
#             "time": now_time,
#             "exercise": exercise["name"].title(),
#             "duration": exercise["duration_min"],
#             "calories": exercise["nf_calories"]
#         }
#     }

#     sheet_response = requests.post(sheet_endpoint, json=sheet_inputs)

#    print(sheet_response.text)
    

# this is fpr analysis.......   
googleSheetId = '1980BeeeYKHyXerBggQJKTpzdibkdfSdX5ORu5cVuRZ0'
worksheetName = 'workouts'
URL = 'https://docs.google.com/spreadsheets/d/{0}/gviz/tq?tqx=out:csv&sheet={1}'.format(
	googleSheetId,
	worksheetName
)
# sample graph not final
df = pandas.read_csv(URL)
print(exercise_text)
x=df["Duration"]
y=df["Calories"]
plt.plot(x, y)
#plt.show()
plt.savefig('PUBLIC/books_read.png')
    
