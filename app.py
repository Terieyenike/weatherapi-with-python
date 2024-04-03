from flask import Flask, render_template, request
from weather import main as get_weather
from infobip_channels.sms.channel import SMSChannel

import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
  data = None
  degree_sign = u"\N{DEGREE SIGN}"
  if request.method == "POST":
    city_name = request.form.get("cityName")
    state_code = request.form.get("stateName")
    country_code = request.form.get("countryName")
    data = get_weather(city_name, state_code, country_code)
    if city_name and state_code and country_code:
      data = get_weather(city_name, state_code, country_code)
      message = f"Weather for {city_name.title()}: temperature of {data.temperature}{degree_sign}C with {data.description}"
      # send_sms_from_app(message)
      print(message)
  return render_template("index.html", data=data)


def send_sms_from_app(text):
    channel = SMSChannel.from_env()
    sms_response = channel.send_sms_message({
        'messages': [{
            'from': 'Real-time weather info',
            'text': text,
            'destinations': [{
                'to': os.environ['DESTINATION_NUMBER']
            }],
        }]
    })
    print(sms_response)
