import requests
from django.core.management.base import BaseCommand
from api_planets.models import Planet

class Command(BaseCommand):
    help = 'Fetch data from the GraphQL endpoint and populate the database'

    def handle(self, *args, **kwargs):
        url = "https://swapi-graphql.netlify.app/.netlify/functions/index"
        query = """
        query {
          allPlanets {
            planets {
              name
              population
              terrains
              climates
            }
          }
        }
        """
        response = requests.post(url, json={'query': query})
        if response.status_code == 200:
            planets = response.json()['data']['allPlanets']['planets']
            self.populate_db(planets)
        else:
            self.stdout.write(self.style.ERROR('Failed to fetch data'))

    def populate_db(self, planets):
        for planet_data in planets:
            Planet.objects.create(
                name=planet_data['name'],
                population=planet_data.get('population'),
                terrains=planet_data['terrains'],
                climates=planet_data['climates']
            )
        self.stdout.write(self.style.SUCCESS('Successfully populated the database'))