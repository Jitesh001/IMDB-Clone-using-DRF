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

- [Register](http://127.0.0.1:8000/api/account/register/): POST request to register a new user
- [Login](http://127.0.0.1:8000/api/account/login/): POST request to log in and obtain a token
- [Logout](http://127.0.0.1:8000/api/account/logout/): POST request with an Authorization token to log out

### Watchlist Management

- [Get All Watchlists](http://127.0.0.1:8000/api/watchlist/): GET request to retrieve all watchlists
- [Get Watchlist by ID](http://127.0.0.1:8000/api/watchlist/5/): GET request to retrieve details of a specific watchlist
- [Create Review for Watchlist](http://127.0.0.1:8000/api/watchlist/9/review-create/): POST request to create a review for a watchlist
- [Get Reviews for Watchlist](http://127.0.0.1:8000/api/watchlist/9/reviews/): GET request to retrieve reviews for a specific watchlist
- [Get User Reviews](http://127.0.0.1:8000/api/watchlist/user-reviews/?username=user4): GET request to retrieve all reviews added by a specific user

### Streaming Platform Management

- [Get All Streaming Platforms](http://127.0.0.1:8000/api/watchlist/stream/): GET request to retrieve a list of all streaming platforms
- [Get Streaming Platform by ID](http://127.0.0.1:8000/api/watchlist/stream/1/): GET request to retrieve details of a specific streaming platform
- [Create Streaming Platform](http://127.0.0.1:8000/api/watchlist/stream/): POST request to add a new streaming platform
- [Update Streaming Platform](http://127.0.0.1:8000/api/watchlist/stream/1/): PUT request to update details of a specific streaming platform
- [Delete Streaming Platform](http://127.0.0.1:8000/api/watchlist/stream/1/): DELETE request to delete a specific streaming platform

### Review Management

- [Get Review by ID](http://127.0.0.1:8000/api/watchlist/reviews/12/): GET request to retrieve details of a specific review
- [Update Review](http://127.0.0.1:8000/api/watchlist/reviews/12/): PUT request to update details of a specific review
- [Delete Review](http://127.0.0.1:8000/api/watchlist/reviews/12/): DELETE request to delete a specific review

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
