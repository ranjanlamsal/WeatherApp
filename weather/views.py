from django.shortcuts import render
import json
import urllib.request

# Create your views here.

def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        res = urllib.request.urlopen('http://api.weatherapi.com/v1/current.json?key=c82dda5ac99f4070857155801222707&q='+city).read()
        json_data = json.loads(res)
        
        data = {
            "country_name": str(json_data.get('location').get('country')),
            "coordinate": 'longitude ' + str(json_data.get('location').get('lon'))+' | latitude '+ str(json_data.get('location').get('lat')),
            "localtime":str(json_data.get('location').get('localtime')),
            "temp" : str(json_data.get('current').get('temp_c'))+ 'C',
            "feels_like": str(json_data.get('current').get('feelslike_c')) + 'C',
            "pressure" : str(json_data.get('current').get('pressure_in')),
            "wind_speed": str(json_data.get('current').get('wind_mph')),
            "wind_dir": str(json_data.get('current').get('wind_dir')),
            "humidity" : str(json_data.get('current').get('humidity')),
            "precip": str(json_data.get('current').get('precip_mm')) +'mm',
        }
    else:
        data = dict()
    return render(request, 'index.html',data)