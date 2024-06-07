from flask import Flask, render_template,request
import requests

app = Flask(__name__)

def get_weather_data(city):
    API_KEY = '44289cc9e0c7a71b0db0d10a93465baf'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={ city }&units=metric&lang=es&appid={API_KEY}'
    r = requests.get(url).json()
    return r 

@app.route("/", methods=['POST','GET'])
def index():
    if request.method == 'POST':
       data = get_weather_data('Guayaquil')
       return render_template('index.html',context=data)
    else:
        return render_template('index.html')

if  __name__ == "__main__":
    app.run(debug=True) 
