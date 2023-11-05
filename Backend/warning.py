# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.environ['ACc7f94c592438bdedb764d05ae4d5b536']
auth_token = os.environ['2790f27c801a91ba08e72f660f15c64a']
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                     from_='+12105260558',
                     to='+16477631216'
                 )

print(message.sid)