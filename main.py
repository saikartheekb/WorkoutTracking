import requests
from datetime import datetime

APPID = '1b003c57'
APIKEY = 'f3875e44e306858b259e7dd9851c3e9c'

endpoint = 'https://trackapi.nutritionix.com/v2/natural/exercise'

headers = {
    'x-app-id': APPID,
    'x-app-key': APIKEY,
    'x-remote-user-id': '0',
}

exercise_text = input("Tell me which exercises you did today:")
exercise = {
    "query": exercise_text,
    "gender": "male",
    "weight_kg": 85.05,
    "height_cm": 171.5,
    "age": 27
}

today = datetime.now().strftime('%d/%m/%Y')
current_time = datetime.now().strftime('%I:%M:%S %p')

print(today, current_time)

response = requests.post(endpoint, headers=headers, json=exercise)

res = response.json()

print(res)
print(response.text)

SHEETY_ENDPOINT = 'https://api.sheety.co/db309d97912bcb6064338e1ccb138add/workoutTracking/workouts'
SHEETY_TOKEN = 'sheetybearer'
SHEETY_AUTHORIZATION = 'Bearer sheetybearer'

sheety_headers = {
    'Token': SHEETY_TOKEN,
    'Authorization': SHEETY_AUTHORIZATION,
}

for exercise_item in res['exercises']:
    params = {
        'workout': {
            'date': today,
            'time': current_time,
            'exercise': exercise_item['name'],
            'duration': exercise_item['duration_min'],
            'calories': exercise_item['nf_calories'],
        }
    }
    sheety_res = requests.post(SHEETY_ENDPOINT, json=params, headers=sheety_headers)
    print(sheety_res.text)
