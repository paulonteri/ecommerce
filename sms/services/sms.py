from datetime import datetime

import africastalking
from django.conf import settings


# Initialize SDK
username = settings.AFRICASTALKING_USERNAME
api_key = settings.AFRICASTALKING_API_KEY
africastalking.initialize(username, api_key)
sms = africastalking.SMS


def send_sms(user, message, recipients):
    """
    Send sms
    """
    recipients = recipients
    message = message
    # time_sent = datetime.now()
    #
    if len(message) > 160:
        raise Exception("Ensure your message has less that 160 characters")

    try:
        # buy a Dedicated Short Code to get a sender ID
        # response = sms.send(message, recipients, sender)
        response = sms.send(message, recipients)
    except Exception as e:
        raise e
    else:
        print(response)
        return response
