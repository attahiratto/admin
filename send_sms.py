import africastalking
aft_sms = africastalking.SMS

class send_sms:
    def __init__(self):
        #1.TODO Add in your details below
        username = ""  # use 'sandbox' for testing
        api_key = ""   # Your api key
        africastalking.initialize(username, api_key)
        
#2.TODO define a function that with no parameters
# and tries to send the using aft_sms.send function which takes in 3 parameters, message,list of recipients and sender 
    def send(self):
        pass


        