import africastalking


class send_sms:
    def __init__(self):
        username = "sandbox"  # use 'sandbox' for test environment
        api_key = "FIll in your key" 
        africastalking.initialize(username, api_key)
        self.sms = africastalking.SMS

    def send(self):
        recipients = ["+2349122073199"]  # your test number in intl format
        message = 'THIS IS A TEST MESSAGE FROM NURTURENET'
        sender = "ANC"  # or your test shortcode/alphanumeric sender ID
        try:
            response = self.sms.send(message, recipients, sender)
            print(response)
        except Exception as e:
            print(f"Houston we have a problem: {e}")

        