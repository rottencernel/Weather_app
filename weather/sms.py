from vonage import Sms
from decouple import config

VONAGE_API_KEY = config('api_key')
VONAGE_API_SECRET = config('api_secret')

sms = Sms(key=VONAGE_API_KEY, secret=VONAGE_API_SECRET)


def send_sms_code(user_number, code):
    sms.send_message({
        "from": 'Weatherapp',
        "to": user_number,
        "text": code,
    })
    return
