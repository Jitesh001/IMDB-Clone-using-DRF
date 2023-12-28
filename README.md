# IMDB-Clone-using-DRF
---

# Django Rest Framework API - IMDB Clone

This project is a Django Rest Framework (DRF) API implementation, inspired by the Udemy course [Django Rest Framework](https://www.udemy.com/course/django-rest-framework/). The course provides a comprehensive guide to building a DRF API project, covering various aspects of development.

## Project Overview

### IMDB Clone using Django Rest Framework

The project involves creating an IMDB clone utilizing four databases:

- Watchlist (stores movies and series details)
- StreamPlatform (stores streaming platform information)
- Review (stores user reviews)
- User (built-in Django Model)

Key features and concepts applied in the project:

- Model serializers for sending requests in JSON format
- Various API views including APIView, generic views, and viewsets
- Throttling to limit the number of requests sent by users
- Different permissions to restrict access for creating watchlists, adding new platforms based on user roles
- Token-based authentication using the built-in Token model for register, login, and logout functionality

## Project Structure

Important folders in the project:

- `user_app`: Files related to user registration, login, and logout
- `watchlist_app`: Main API configuration, API-related routes and settings, and an `api` subfolder containing serializers, views, throttling, and permission files
- `watchmate`: Main project folder with project settings and URLs

## API Endpoints

### [Django RestFramework Admin Dashboard](http://127.0.0.1:8000/dashboard/)

- Admin dashboard displaying a list of users with passwords in the database

### User Authentication

- http://127.0.0.1:8000/dashboard/
Django RestFramework Admin dashboard. List of users with passwords in the database. [(watchappadmin, admin@123), (user1, user2, user4, user5, user6, user7, user8 have same password  = Abc@1234), 

- http://127.0.0.1:8000/api/account/register/
POST - Body > Formdata - provide key-value pair(username, password, password2, email), once send req you get token to access other API urls

- http://127.0.0.1:8000/api/account/login/
POST - Body > Formdata - provide key-value pair needed (username, password, password2), once sent req you get a token to access other API urls.

- http://127.0.0.1:8000/api/account/logout/
POST - Headers > Provide Key-Value pair (Authorization - token value), once req sent, you get logout.

### Watchlist Management

- http://127.0.0.1:8000/api/watchlist/
GET - get all watchlist - any user can access it, no token authentication
Anonymous users can send 10 req/day, registered users with token authentication can send 100 req/day.
POST - only admin can add new watchlist (movies/series)

- http://127.0.0.1:8000/api/watchlist/5/ - here 5 is watchlist id
GET - Get all the reviews for the particular watchlist id.
Anonymous user can send 10 req/day, registered user with token authentication can send 100 req/day
DELETE - Only admin can Delete the watchlist with specified ID.

### Streaming Platform Management

- http://127.0.0.1:8000/api/watchlist/stream/
GET - get list of all streaming platforms with available watchlist
POST - add new streaming platform, only admin can add new platform, authentication token required.

- http://127.0.0.1:8000/api/watchlist/stream/1/ - here 1 is stream ID
GET - get details of particular streaming platform with ID provided.
DELETE/PUT - add new streaming platform, only admin can add/DELETE new platform, authentication token required.


### Review Management

- http://127.0.0.1:8000/api/watchlist/9/review-create/ - here 9 is Watch ID
POST - authenticated user can only create a review, one review/watchlist.

- http://127.0.0.1:8000/api/watchlist/9/reviews/  - here 9 is watchlist id
GET - get all reviews related to specific watchlist id. Only token authenticated users can access it, 100 req/day.

- http://127.0.0.1:8000/api/watchlist/reviews/12/ - 12 is Review ID
GET - Get details of review based on provided id
DELETE/PUT - only admin or user who created review can edit it, authentication token required.

- http://127.0.0.1:8000/api/watchlist/user-reviews/?username=user4
user4  is username
GET - get all the reviews added by the provided user.

## Testing API Endpoints

To test the API endpoints, it is recommended to use Postman. Follow the provided instructions for providing a token in the Postman API for authentication.

## How to Run the Project Locally

### Prerequisites:

- Git and Python installed globally

### Steps:

1. Clone the repository:

    ```bash
    git clone https://github.com/Jitesh001/IMDB-Clone-using-DRF.git
    ```

2. Navigate to the project folder and create a virtual environment:

    ```bash
    python -m venv watchappenv
    ```

3. Activate the virtual environment:

    - On Windows:

        ```bash
        .\watchappenv\Scripts\activate
        ```

    - On macOS and Linux:

        ```bash
        source watchappenv/bin/activate
        ```

4. Install required packages:

    ```bash
    pip install -r requirements.txt
    ```

5. Run the project:

    ```bash
    python manage.py runserver
    ```

6. Test the API endpoints in Postman or any other API tool.

Note: The base URL `http://127.0.0.1:8000` may change based on your local settings. Replace it with the URL you get after running the project.

---

Feel free to customize the README file further based on your preferences or additional details you want to include.
