import os
from flask import Flask, request,Response
#3.TODO inmport send_sms

app = Flask(__name__)

@app.route('/incoming-messages', methods=['POST'])
def incoming_messages():
   pass 


@app.route('/delivery-reports', methods=['POST'])
def delivery_reports():
   pass

if __name__ == "__main__":
    
    app.run(debug=True)