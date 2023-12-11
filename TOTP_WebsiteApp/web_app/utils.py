
from twilio.rest import Client
from django.conf import settings

def send_sms(to, message):
    client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
    from_number = settings.TWILIO_PHONE_NUMBER

    message = client.messages.create(
        to=to,
        from_=from_number,
        body=message
    )

    return message.sid
