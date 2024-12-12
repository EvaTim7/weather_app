from flask import Flask, render_template, request
from weather import get_current_weather
from waitress import serve

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/weather')
def get_weather():
    city = request.args.get('city')

    weather_data = get_current_weather(city)
    if weather_data["cod"] == 200:
        return render_template("weather.html",
                                city_name=weather_data["name"],
                                temp=weather_data["main"]["temp"],
                                cod=weather_data["cod"])
    else:
        return render_template("weather.html", 
                               cod=weather_data["cod"],
                               error=weather_data["message"])


if __name__ == "__main__":
    serve(app,debug=True, host="0.0.0.0", port=8000)
    #app.run(debug=True, host="0.0.0.0", port=8000)