# utils.py file defined for the Twilio API. This file contains a function to send an SMS using the Twilio API. The function takes two parameters: phone_number and message. The phone_number parameter is the recipient's phone number, and the message parameter is the message to be sent. The function initializes the Twilio client with the credentials from the settings file and sends the SMS using the client. If the SMS is sent successfully, the function returns True; otherwise, it returns False.

from twilio.rest import Client
from django.conf import settings

def send_sms(phone_number, message):
    try:
        # Initialize Twilio client with your credentials
        client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)

        # Send the SMS
        client.messages.create(
            to=phone_number,
            from_=settings.TWILIO_PHONE_NUMBER,
            body=message
        )

        return True  # SMS sent successfully
    except Exception as e:
        print(f"Error sending SMS: {e}")
        return False  # SMS sending failed
