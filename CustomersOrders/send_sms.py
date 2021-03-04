# import package
import africastalking
from decouple import config


def SendSMS(username, phone_number, item, amount):
    # Initialize SDK
    at_username = config('SANDBOX_USERNAME')    # use 'sandbox' for development in the test environment
    api_key = config('SANDBOX_API_KEY')      # use your sandbox app API key for development in the test environment
    africastalking.initialize(at_username, api_key)

    # Initialize a service e.g. SMS
    sms = africastalking.SMS
    
    
    message = f'Hi {username}. Your order of {item}, Kshs. {amount}, has been received and is being processed. Thank you.'
    sender = 12376
    # Use the service synchronously
    response = sms.send(message, [phone_number], sender)
    print(response)

     