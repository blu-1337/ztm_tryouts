# to be able to send this message, the phone number needs to be verified first

# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client

# Find your Account SID and Auth Token in Account Info
# and set the environment variables. See http://twil.io/secure
account_sid = os.environ['TWILIO_ACCOUNT_SID'] = 'AC2f589c48b38782c61f0539ded7c2127b'
auth_token = os.environ['TWILIO_AUTH_TOKEN'] = 'bf7d6713f411960686924ecaa111e035'
client = Client(account_sid, auth_token)

message = client.messages.create(
  body='Hi there',
  from_='+14246227129',
  to='+40727292100'
)

print(message.sid)
