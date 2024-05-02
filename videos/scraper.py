import logging
from typing import Optional

from django.db import transaction

from videos.models import Topic, Video
from videos.youtube_client import search_videos


logger = logging.getLogger(__name__)


def _youtube_video_url(video_id: str) -> str:
    return f"https://www.youtube.com/watch?v={video_id}"


def _youtube_video_to_video_model(video: dict, topic: Topic) -> Optional[Video]:
    """
    Youtube video structure:
        {
            "kind": "youtube#searchResult",
            "etag": "HPqmSN-UeDpCCQCPdKld4_9Fkp4",
            "id": {
                "kind": "youtube#video",
                "videoId": "7YugHTWIvC0"
            },
            "snippet": {
                "publishedAt": "2023-02-27T00:06:27Z",
                "channelId": "UCbdRpDTurLQF9tCutZr3qmw",
                "title": "Motivating Black Men: Overcoming Adversity and Achieving Success",
                "description": "Welcome to this inspiring video on Motivating Black Men: Overcoming Adversity and Achieving Success. In this video, we will be ...",
                "thumbnails": {
                    "default": {
                        "url": "https://i.ytimg.com/vi/7YugHTWIvC0/default.jpg",
                        "width": 120,
                        "height": 90
                    },
                    "medium": {
                        "url": "https://i.ytimg.com/vi/7YugHTWIvC0/mqdefault.jpg",
                        "width": 320,
                        "height": 180
                    },
                    "high": {
                        "url": "https://i.ytimg.com/vi/7YugHTWIvC0/hqdefault.jpg",
                        "width": 480,
                        "height": 360
                    }
                },
                "channelTitle": "Black Getabout ",
                "liveBroadcastContent": "none",
                "publishTime": "2023-02-27T00:06:27Z"
            }
        }
    """
    if "videoId" not in video["id"]:
        return None

    return Video(
        videoId=video["id"]["videoId"],
        title=video["snippet"]["title"],
        description=video["snippet"]["description"],
        channel_title=video["snippet"]["channelTitle"],
        channel_id=video["snippet"]["channelId"],
        published_at=video["snippet"]["publishedAt"],
        url=_youtube_video_url(video["id"]["videoId"]),
        topic=topic,
    )


@transaction.atomic
def process_topic(topic: Topic):
    """
    Deletes all the videos for a topic, retrieves all the videos again and saves them
    """
    logger.info("Processing topic %s", topic)
    Video.objects.filter(topic=topic).delete()
    videos = search_videos(topic.search_prompt)
    for video in videos:
        video_model = _youtube_video_to_video_model(video, topic)
        if video_model:
            video_model.save()
