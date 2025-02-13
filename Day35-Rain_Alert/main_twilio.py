import os
import requests
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient # for pythonanywhere free account


OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
#api_key = "some_api_key"
api_key = os.environ.get("OWM_API_KEY")
account_sid = 'some_sid'
auth_token = os.environ.get('AUTH_TOKEN')

weather_params = {
    "lat":51.507351,
    "lon":-0.127758,
    "appid":api_key,
    "cnt":4,
}

def send_twillio_message(messageX):

    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies= {'https':os.environ['https_proxy']}

    client = Client(account_sid, auth_token, http_client=proxy_client)

    message = client.messages.create(
        body=messageX,
        from_ = '+123231231231',
        to='+33333333333')
    print(message.status)

response = requests.get(OWM_Endpoint, params= weather_params)
response.raise_for_status()

weather_data=response.json()

list_of_twelve_hours = weather_data["hourly"][0:12]
will_rain = False

for hour in list_of_twelve_hours:
    condition_code = hour["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    message = "It's going to rain, don't forget to bring an umbrella!"
    send_twillio_message(message)
