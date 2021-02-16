from flask import Flask, jsonify
from flask import Response,json

from flask import Flask, render_template, request, redirect

from datetime import datetime
import joblib
import requests

#################################################
# Flask Setup
#################################################
app = Flask(__name__)
TODAYS_DATA = None

#################################################
# Flask Routes
#################################################

@app.route("/",methods=['GET',"POST"])
def home():
    apiKey = "8a1225ee25da9bd6028df45cea70df26"
    url = f"https://api.openweathermap.org/data/2.5/onecall?lat=-37.81&lon=144.96&units=metric&exclude=minute,hourly,current,alerts&appid={apiKey}";

    response = requests.get(url).json()
    global TODAYS_DATA
    TODAYS_DATA = response["daily"][0]
    forecast = TODAYS_DATA["weather"][0]["main"]
    description = TODAYS_DATA["weather"][0]["description"]
    
    icon_id = TODAYS_DATA["weather"][0]["icon"]
    icon = f"http://openweathermap.org/img/wn/{icon_id}@2x.png"
    
    try:
        rain = TODAYS_DATA["rain"]
    except:
        rain = "0"

    return render_template("index.html", today=TODAYS_DATA, rain=rain, forecast = forecast, description=description, icon_id=icon)



@app.route("/predict",methods=['GET',"POST"])
def predict():
    apiKey = "8a1225ee25da9bd6028df45cea70df26"
    url = f"https://api.openweathermap.org/data/2.5/onecall?lat=-37.81&lon=144.96&units=metric&exclude=minute,hourly,current,alerts&appid={apiKey}"

    response = requests.get(url).json()
    global TODAYS_DATA
    TODAYS_DATA = response["daily"][0]
    today = TODAYS_DATA

    day = datetime.today()
    datem = datetime(day.year, day.month, 1)
    month = datem.month

    try:
        rain = TODAYS_DATA["rain"]
    except:
        rain = int(0)

    if rain > 1:
        rain_today = 1
    else:
        rain_today = int(0)

    feature_list = [today["temp"]["min"], today["temp"]["min"], rain, today["wind_speed"], rain_today,today["clouds"], today["humidity"], today["pressure"],month]
    model = joblib.load("weather_predictor.sav")
    k = model.predict([feature_list])

    return (jsonify(str(k)))

if __name__ == '__main__':
	app.run(debug=True)