import os
from flask import Flask, request,Response,render_template
from send_sms import send_sms

app = Flask(__name__)

@app.route('/incoming-messages', methods=['POST'])
def incoming_messages():
   pass 


@app.route('/delivery-reports', methods=['POST'])
def delivery_reports():
   pass
@app.route('/')
def index():
    return render_template('home.html')
@app.route('/map')
def map():
    return render_template('map.html')
@app.route('/send')
def sms():
    send_sms().send()
    return "Message Sent"
@app.route('/appointments')
def appointments():
    return render_template('appointments.html')
@app.route('/exports')
def exports():
    return render_template('exports.html')
@app.route('/sms')
def sms_page():
    return render_template('sms.html')
@app.route("/ussd", methods = ['POST', 'GET'])
def ussd():
    # Read the variables sent via POST from our API
    session_id   = request.values.get("sessionId", None)
    serviceCode  = request.values.get("serviceCode", None)
    phone_number = request.values.get("phoneNumber", None)
    text         = request.values.get("text", "")  # use empty string as default
    USER = {}
    parts = text.split('*') if text != '' else []
    step = len(parts)

    # First request
    if text == '':
        response  = "CON Welcome to NurtureNet Please select your preferred language \n"
        response += "1. English \n"
        response += "2. Hausa \n"
        response += "3. Yoruba \n"

    # English selected -> show main menu
    elif parts[0] == '1' and step == 1:
        response  = "CON Welcome, what would like to do? \n"
        response += "1. Register \n"
        response += "2. Login \n"

    # Hausa selected -> show main menu (Hausa)
    elif parts[0] == '2' and step == 1:
        response  = "CON Barka da zuwa NurtureNet. Zaɓi aikin da kake so:\n"
        response += "1. Sabon Rajista \n"
        response += "2. Shiga (Login) \n"

    # English: Register flow (1 -> 1)
    elif step >= 2 and parts[0] == '1' and parts[1] == '1':
        if step == 2:
            response = "CON Please enter your full name"
        elif step == 3:
            USER['name'] = parts[2]
            response = "CON Please enter your age"
        elif step == 4:
            USER['age'] = parts[3]
            response = "CON Please enter your phone number (include country code if required)"
        elif step == 5:
            USER['phone'] = parts[4]
            response = "END Registration successful. Thank you!"
        else:
            response = "END Invalid registration step"

    # English: Login flow (1 -> 2)
    elif step >= 2 and parts[0] == '1' and parts[1] == '2':
        
        if step == 2:
            response = "CON Please enter your phone number to login"
        
        elif step == 3:
            response = "END Login successful. Welcome USER"
  
        else:
            response = "END Invalid login step"

    # Hausa: Register flow (2 -> 1)
    elif step >= 2 and parts[0] == '2' and parts[1] == '1':
        if step == 2:
            response = "CON Don Allah shigar da cikakken sunanka"
        elif step == 3:
            USER['name'] = parts[2]
            response = "CON Don Allah shigar da shekarunka"
        elif step == 4:
            USER['age'] = parts[3]
            response = "CON Don Allah shigar da lambar wayarka (tare da lambar ƙasa idan akwai)"
        elif step == 5:
            USER['phone'] = parts[4]
            response = "END Rajistar ka yi nasara. mun gode!"
        else:
            response = "END Mataki mara kyau na rajista"

    # Hausa: Login flow (2 -> 2)
    elif step >= 2 and parts[0] == '2' and parts[1] == '2':
       
        if step == 2:
            response = "CON Don Allah shigar da lambar wayarka domin shiga"
        elif step == 3:
            response = "CON Barka da zuwa NurtureNet. Zaɓi aikin da kake so:\n"
            response += "1. saduwa na gaba  \n"
            response += "2. rigakafin yara \n"
            response += "3. asibitin mafi kusa \n"
            response += "4. chanza yare \n"
        elif step == 4 and parts[3] == '1':
            response = "END Your next appointment is on 27th Dec 2025"
        elif step == 4 and parts[3] == '3':
                response = "END The nearest clinic is HealthCare Clinic, 123 Yakubu Gowon Way kaduna"
        elif step == 4 and parts[3] == '2':
            response = "CON 1. Register child \n"
            response += "2. View next schedule \n"
            if step == 5 and parts[3] == '2' and parts[4] == '1':
                response = "END Child registered successfully"
            elif step == 5 and parts[3] == '2' and parts[4] == '2':
                response = "END Your child's next vaccine is on 15th Jan 2026"
            
        
        else:
            response = "END Ba daidai ka shiga ba🙄"

    else:
        response = "END Invalid choices"

    return response
    

if __name__ == "__main__":
    
    app.run(debug=True)