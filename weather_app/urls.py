from django.urls import path
from . import views as core_views
from . import views
from .views import SearchResultsView

urlpatterns = [
    path('weather/<int:city_ID>', views.index, name = 'weather'), 
    path('', core_views.cities_view, name='cities'),
    path('weather/<int:city_ID>/<int:date>', views.weather_select, name = 'weather_select'),
    path('test/', views.test, name = 'test'),
    path("search/", SearchResultsView.as_view(), name="search_results"),
    ]
