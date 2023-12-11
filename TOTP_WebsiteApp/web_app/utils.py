# utils.py

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
