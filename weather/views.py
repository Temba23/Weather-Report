from django.shortcuts import render, HttpResponse
import requests
import datetime
# Create your views here.
def home(request):
    
    if 'city' in request.POST:
        city = request.POST['city']
    else:
        city = 'kathmandu'
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=01815cd21ffd649a0f140b9115961fd1"
    PARAMS = {'units':'metric'}


    response = requests.get(url, params=PARAMS)
    data = response.json()
    try:
        description = data['weather'][0]['description']
        icon = data['weather'][0]['icon']
        temp = data['main']['temp']

        day = datetime.date.today()

        return render(request, 'index.html', {'description':description, 'icon':icon, 'temp':temp, 'day':day, 'city':city})
    except:
        return HttpResponse("Provided City is not in API.")