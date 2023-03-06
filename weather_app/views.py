from django.shortcuts import render
import requests
from django.http import HttpResponse
from .models import City
from django.views.generic import TemplateView, ListView
from django.db.models import Q
from django.views.generic.detail import DetailView
from django.template.loader import render_to_string
from django.http import JsonResponse
from datetime import datetime
import environ

# takes: an http request and a city_ID 
# the city_ID is used to get a unique city from the db
# returns: index.html with context
def index(request, city_ID):
    
    env = environ.Env()
    environ.Env.read_env()
    
    # api url, this url is for the 5 day prediction
    url = 'https://api.openweathermap.org/data/2.5/forecast?lat={}&lon={}&appid={}&units=imperial'    
    
    api_key = env('WEATHER_API_KEY') # protect api key
    mydata = City.objects.filter(city_id = city_ID).values()  # getting the unique city from the database
    latitude = mydata[0]['lat']     # getting lat from city data
    longitude = mydata[0]['lng']    # getting lat from city data
    city = mydata[0]['name']        # getting city name from city data

    city_weather = requests.get(url.format(latitude, longitude, api_key)).json() #request the API data and convert the JSON to Python data types
    context = {}    # setting dictionaries for later use
    weather = {}
    
    counter = 0 # increment for the loop
    
    for element in city_weather['list']:
        if counter % 8 == 0:      # allows us to get a single time per day
            date = element['dt']  # get date from data
            date_final = datetime.utcfromtimestamp(date).strftime('%A, %b %-d') # date formatting from unix time
            
            # for each day we create a separate dictionary
            weather = {
                'city' : city,
                'temperature' : element['main']['temp'],
                'description' : element['weather'][0]['description'],
                'icon' : element['weather'][0]['icon'],
                'date' : date_final,
                'date_unix' : element['dt'],
                'city_id' : city_ID
             }
            context[counter] = weather # counter increments by eight: 0, 8, 16, 24, 32 for indices
        counter = counter + 1
    
    return render(request, 'weather_app/index.html', context)

# takes: an http request, a city id number, and a date in unix
# the city_ID is used to get a unique city from the db
# date is passed to the function so we can use it in the weather_select.html 
# returns: weather_select.html with context
def weather_select(request, city_ID, date):
    # api url, this url is for the current time prediction
    url = 'https://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&appid={}&units=imperial'
    
    # get .env contents
    env = environ.Env()
    environ.Env.read_env()
    
    # similar setup to the index view, except we don't loop here since we only need to return one weather data set
    api_key = env('WEATHER_API_KEY')                            # set api key securely
    mydata = City.objects.filter(city_id = city_ID).values()    # get unique city
    latitude = mydata[0]['lat']                                 # get lat from data
    longitude = mydata[0]['lng']                                # get long from data
    city = mydata[0]['name']                                    # get name from data
    city_weather = requests.get(url.format(latitude, longitude, api_key)).json() #request the API data and convert the JSON to Python data types
    date_final = datetime.utcfromtimestamp(date).strftime('%A, %b %-d') # format date from input date   
    print(date_final)
    
    # put everything into a dictionary
    weather = {
        'city' : city,
        'temperature' : city_weather['main']['temp'],
        'description' : city_weather['weather'][0]['description'],
        'icon' : city_weather['weather'][0]['icon'],
        'max_temp' : city_weather['main']['temp_max'],
        'min_temp' : city_weather['main']['temp_min'],
        'humidity' : city_weather['main']['humidity'],
        'date' : date_final
    }
    
    # put into context for html use
    context = {'weather' : weather}
    
    return render(request, 'weather_app/weather_select.html', context)

# takes: an http request
# AJAX call stuff
# returns: cities.html with context
def cities_view(request):
    # context dict for later user
    ctx = {}
    
    # capturing the GET parameter from url
    url_parameter = request.GET.get("q")

    # if there is a search parameter we filter the list
    if url_parameter:
        cities = City.objects.filter(name__icontains=url_parameter)
    # else, we just get all the items from the db
    else:
        cities = City.objects.all()

    # set context
    ctx["cities"] = cities
    
    # checking to see if the request accepts json
    does_req_accept_json = request.accepts("application/json")
    # getting header 
    is_ajax_request = request.headers.get("x-requested-with") == "XMLHttpRequest" and does_req_accept_json

    # check to see if the request is an ajax request
    # pass json response dictionary with a template and context
    if is_ajax_request:
        html = render_to_string(
            template_name="weather-results-partial.html", context={"cities": cities, "q": Q}
        )
        data_dict = {"html_from_view": html}
        return JsonResponse(data=data_dict, safe=False)
    
    return render(request, "cities.html", context=ctx)

# not needed
def test(request):
    city=City.objects.all()
    return render(request,'test.html',{'city':city})

# view for rendering the search results page.
# filters through the database and returns a list of cities with similar names
class SearchResultsView(ListView):
    model = City
    template_name = "search_results.html"

    def get_queryset(self):  # new
        query = self.request.GET.get("q")
        object_list = City.objects.filter(Q(name__icontains=query))
        return object_list