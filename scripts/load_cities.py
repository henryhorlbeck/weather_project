from weather_app.models import City
import csv

# data from: https://simplemaps.com/data/world-cities

def run():
    

    with open('scripts/worldcities.csv') as file:
        reader = csv.reader(file)
        next(reader)  # Advance past the header

        City.objects.all().delete()

        for row in reader:
            
            city = City(name=row[0],
                        name_asci=row[1],
                        lat=row[2],
                        lng=row[3],
                        country=row[4],
                        iso2=row[5],
                        iso3=row[6],
                        admin_name=row[7],
                        capital=row[8],
                        population="1", # some population numbers are unavailable, so just set to 1
                        city_id = row[10]
                        )
            city.save()