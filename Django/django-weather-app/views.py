import requests
from django.shortcuts import render

def home(request):
    context = {}
    city = request.GET.get("city")

    if city:
        api_key = "c3b1ab6d94240baadda98ba066ab02a7"
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        response = requests.get(url).json()

        if response.get("cod") != "404":
            context = {
                "city": city.title(),
                "temp": response["main"]["temp"],
                "feels_like": response["main"]["feels_like"],
                "humidity": response["main"]["humidity"],
                "desc": response["weather"][0]["description"].title(),
                "icon": response["weather"][0]["icon"],
            }

    return render(request, "weather/home.html", {"weather": context})
