# Planets API

This project is designed to address a specific challenge by creating an API that allows for the listing of all planets. It utilizes Django and Django REST Framework (DRF) to efficiently solve the problem and provide a robust backend solution.

## Technologies Used

- **Django**: A high-level Python web framework that encourages rapid development and clean, pragmatic design.
- **Django REST Framework (DRF)**: A powerful and flexible toolkit for building Web APIs in Django, making it easier to create RESTful APIs.
- **SQLite**: A C-language library that implements a small, fast, self-contained, high-reliability, full-featured, SQL database engine.
- **Docker**: A platform for developing, shipping, and running applications in containers.

## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

- Docker

### Installation

1. Clone the repository
   ```sh
   git clone git@github.com:adcc662/planets_graphql.git
   ```
   
2. Enter the project directory
   ```sh
   cd planets_graphql
   ```
   
3. Run the migrations and then start the server
   ```sh
   docker-compose run web python manage.py makemigrations api_planets
   docker-compose run web python manage.py migrate
   docker-compose run web python manage.py fetch_data
   docker-compose up --build
   ```
   
4. The API should now be available at `http://localhost:8000/api_planets/`