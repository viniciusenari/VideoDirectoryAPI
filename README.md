# Videos API
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray)
![MongoDB](https://img.shields.io/badge/MongoDB-%234ea94b.svg?style=for-the-badge&logo=mongodb&logoColor=white)
![Redis](https://img.shields.io/badge/redis-%23DD0031.svg?style=for-the-badge&logo=redis&logoColor=white)
## Introduction
This application is a REST API that allows users to index video information separated in categories.
## Project Support Features
* Users can store and retrieve videos information.
* Users can store and retrieve video categories information.
* Users can get a list of videos separated by category.
* Public (non-authenticated) users can get information from a limited set of videos.
* Pagination, search, throttling, and caching.
## Technologies Used
* [Python](https://www.python.org/) - Programming language.
* [Django Rest Framework](https://www.django-rest-framework.org/) - This is a powerful and flexible toolkit for building Web APIs. It is used to build APIs in Django.
* [MongoDB/MongoDB Atlas](https://www.mongodb.com/) - Free open source NOSQL cross-platform document-oriented database with scalability and flexibility. Data are stored in flexible JSON-like documents. MongoDB Atlas is a cloud-hosted database service for MongoDB.
* [Redis](https://redis.io/) - An open source (BSD licensed), in-memory data structure store, used as a database, cache and message broker. In this project is is being used to cache data.
## Installation Guide
* Clone this repository.
```bash
git clone https://github.com/viniciusenari/videos-api.git
```
* Create a virtual environment.
```bash
python3 -m venv venv
```
* Activate the virtual environment.
```bash
source venv/bin/activate
```
Or, if you are using Windows:
```cmd
venv/bin/activate
```
* Install the dependencies.
```bash
pip install -r requirements.txt
```
* Rename the .env.example to a .env file and add the following environment variables.
```
DEBUG=True
SECRET_KEY=your_secret_key
ALLOWED_HOSTS=*
DATABASE_URL=your_database_url
REDIS_URL=your_redis_url
```
* Run the migrations
```bash
python manage.py migrate
```
## How to use
* Start Redis server.
* Start the Django development server.
```bash
python manage.py runserver
```
## API Endpoints
| HTTP Verbs | Endpoints | Action | Parameters |
| --- | --- | --- | --- |
| GET | /categories/ | Retrieve a list of categories | ?page
| POST | /categories/ | Create a new category |
| GET | /categories/{id}/ | Retrieve a single category |
| PUT | /categories/{id}/ | Update a single category |
| PATCH | /categories/{id}/ | Partially update a single category |
| DELETE | /categories/{id}/ | Delete a single category |
| GET | /categories/{id}/videos | Retrieve a list of videos in the same categories | ?page
| GET | /videos/ | Retrieve a list of videos | ?search, ?page |
| GET | /videos/free | Retrieve a list of videos for unauthenticated users |
| POST | /videos/ | Create a new video |
| GET | /videos/{id}/ | Retrieve a single video |
| PUT | /videos/{id}/ | Update a single video |
| PATCH | /videos/{id}/ | Partially update a single video |
| DELETE | /videos/{id}/ | Delete a single video |

## Documentation
You can view the API documentation created with Swagger and Redoc through the endpoints /swagger/ and /redoc/.

## License
This project is available for use under the MIT License.
