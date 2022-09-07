import os
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = "YOur account_sid"
auth_token = "Your auth token"
client = Client(account_sid, auth_token)
def send_sms(user_code,phone_number):
    message = client.messages \
                    .create(
                         body=f"Hi! Your user verification code is:  {user_code}",
                         from_='Your Phone Number From Twillio',
                         to=phone_number
                     )

    print(message.sid)