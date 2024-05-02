# Video searcher
This is a simple video searcher that searches for videos using the YouTube API and saves them into a Postgres database.

## Installation

- Make sure you have Docker installed. If not, you can download it from https://www.docker.com/get-started.
- Get a YouTube API key from https://console.developers.google.com/. You will have to create a project and enable the YouTube API.
- Create an `.env` file in the root directory, by copying and renaming the `.env.example` file and add the YouTube API key in the `YOUTUBE_API_KEY` variable. The rest of variables are OK for local testing.
- Create a `dbdata` folder in the root directory.
- Run `docker compose up -d`. Wait for the containers to start (check with `docker compose logs` or `docker ps`).
- Run `docker compose exec backend python manage.py migrate`.
- Run `docker compose exec backend python manage.py createsuperuser` and follow the instructions to create a superuser.
- Run `docker compose exec backend python manage.py loadTopics` to load the topics into the database.
- Open http://localhost:8000/admin/ in the browser.

## How does it work

- There are two tables in the database: `Topic` and `Video`.
- The `Topic` table contains the topics that the user can search for. We use the `search_prompt` field to search for videos using the YouTube API. Feel free to use the Django Admin site to change the search_prompt field and evaluate the results.
- In http://localhost:8000/admin/, once logged in with the superuser credentials, you can navigate to the topics list page.
- There, you can select one or more topics and then execute the custom action `Retrieve videos for the selected topics`.
- This action executes a background task for each topic, deletes all the existing videos for that topic, searches for new videos using the YouTube API and saves them into the database. It searches 25 items per topic.
- Wait for the background tasks to finish (it takes only some seconds for all the topics).
- You can check the videos in the Videos page, or in the Topic detail page.

Take into account the YouTube API is free, but it has some rate limitations. If you execute the process too many times in a short period, you may get an error from the API.

## Architecture

- Backend: Django application.
- Database: Postgres.
- Background task execution: Celery with Redis as broker.

All these components are executed in Docker containers by using docker compose.