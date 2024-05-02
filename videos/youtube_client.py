import requests
from django.conf import settings

MAX_RESULTS = 25


def search_videos(search_prompt):
    """
    Function to search for videos on Youtube based on a search prompt.
    """
    # Set the API key and the search prompt.
    api_key = settings.YOUTUBE_API_KEY
    url = (
        "https://youtube.googleapis.com/youtube/v3/search?part=snippet&"
        f"maxResults={MAX_RESULTS}&q={search_prompt}&key={api_key}"
    )
    response = requests.get(url)
    response.raise_for_status()
    return response.json()["items"]
