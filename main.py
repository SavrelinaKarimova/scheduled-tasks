import requests 
import os
from twilio.rest import Client

OWM_Endpoint = 'https://api.openweathermap.org/data/2.5/forecast'
api_key = os.environ.get("OWM_API_KEY")
account_sid = os.environ.get("ACCOUNT_ID")
auth_token = os.environ.get("AUTH_TOKEN")

parameters = {
    'lat' :  26.820553, 
    'lon' :  30.802498, 
    'appid': api_key,
    'cnt': 4, 
}

response = requests.get(OWM_Endpoint, params=parameters)
response.raise_for_status
weather_data = response.json() 


will_rain = False
for hour_data in weather_data['list']: 
    condition_code = hour_data['weather'][0]['id']
    print(condition_code)
    if condition_code < 700:
        will_rain = True
        
        

if will_rain: 
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_= os.environ.get("TWILIO_VER_NUM"),
        body="It's going to rain today. Remember to bring an umbrella☔️",
        to= os.environ.get("TWILIO_MY_NUM")
        )
    print(message.status)
