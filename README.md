# Django Location API

## API endpoint
Location API can be reached at http://127.0.0.1:8000/locations
### Query parameters
* Location coordinates
* Search radius (in metres)
* Category (optional, exact match only)
* Maximum result count (integer)

example URL: http://127.0.0.1:8000/locations?category=restaurant&coords=43.895776,-79.464448&count=2&radius=10000

## How to run
Requirements are Python, Django and DRF (Django Rest Framework)
1. After installing requirements, run `python manage.py runserver`
