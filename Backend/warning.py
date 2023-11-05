import os

from flask import Flask, request, jsonify, render_template
from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException

app = Flask(__name__)

# Your Twilio Account SID and Auth Token
TWILIO_ACCOUNT_SID = "ACc7f94c592438bdedb764d05ae4d5b536"
TWILIO_AUTH_TOKEN = "2790f27c801a91ba08e72f660f15c64a"

# Initialize the Twilio client
twilio_client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_sms', methods=['POST'])
def send_sms():
    try:
        data = request.get_json()
        phone_number = data.get('phoneNumber')
        
        # Send an SMS using Twilio
        message = twilio_client.messages.create(
            to="+16477631216",  # Replace with the recipient's phone number
            from_="+12105260558",  # Your Twilio phone number
            body="Emergency! This is a test SMS from your TTC Safety app."
        )

        return jsonify({"status": "success", "message": f"SMS sent to {phone_number}"})
    except TwilioRestException as e:
        return jsonify({"status": "error", "message": str(e)}, 400)
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}, 500)

if __name__ == '__main__':

    app.run(debug=True, port=5000)
