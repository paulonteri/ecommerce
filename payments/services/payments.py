# Import the Africa's Talking SDK
import africastalking

from django.conf import settings

# Initialize the SDK
username = settings.AFRICASTALKING_USERNAME
api_key = settings.AFRICASTALKING_API_KEY
africastalking.initialize(username, api_key)

payments = africastalking.Payment
product_name = settings.AFRICASTALKING_PAYMENT_PROD_NAME

# 3 letter ISO currency code
currency_code = settings.AFRICASTALKING_CURRENCY


def mobile_payments(phone_number, amount):
    """"
    Takes in:
    phone number you want and set it to the international format eg: "+254703130580"
    """

    # Metadata which will be resent back in the final payment notification
    metadata = {
        "agentId": "",
        "productId": ""
    }

    try:
        res = payments.mobile_checkout(product_name, phone_number, currency_code, amount, metadata)
        print(res)
    except Exception as e:
        print(f"Something went wrong: {e}")
