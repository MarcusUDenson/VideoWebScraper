from unittest import mock

from django.test import TestCase
from videos.models import Topic
from videos.scraper import process_topic


class ScraperTestCase(TestCase):
    @mock.patch("videos.scraper.search_videos")
    def test_save_videos_for_topic(self, mock_search_videos):
        mock_search_videos.return_value = [
            {
                "kind": "youtube#searchResult",
                "etag": "HPqmSN-UeDpCCQCPdKld4_9Fkp4",
                "id": {"kind": "youtube#video", "videoId": "7YugHTWIvC0"},
                "snippet": {
                    "publishedAt": "2023-02-27T00:06:27Z",
                    "channelId": "UCbdRpDTurLQF9tCutZr3qmw",
                    "title": "Motivating Black Men: Overcoming Adversity and Achieving Success",
                    "description": "Welcome to this inspiring video on Motivating Black Men: Overcoming Adversity and Achieving Success. In this video, we will be ...",
                    "thumbnails": {
                        "default": {
                            "url": "https://i.ytimg.com/vi/7YugHTWIvC0/default.jpg",
                            "width": 120,
                            "height": 90,
                        },
                        "medium": {
                            "url": "https://i.ytimg.com/vi/7YugHTWIvC0/mqdefault.jpg",
                            "width": 320,
                            "height": 180,
                        },
                        "high": {
                            "url": "https://i.ytimg.com/vi/7YugHTWIvC0/hqdefault.jpg",
                            "width": 480,
                            "height": 360,
                        },
                    },
                    "channelTitle": "Black Getabout ",
                    "liveBroadcastContent": "none",
                    "publishTime": "2023-02-27T00:06:27Z",
                }
            },
            {
                "kind": "youtube#searchResult",
                "etag": "AyxKeMLsGMj_XfhZhR299ZGW3uM",
                "id": {
                    "kind": "youtube#video",
                    "videoId": "nIu8GZH54OA"
                },
                "snippet": {
                    "publishedAt": "2022-07-25T16:50:50Z",
                    "channelId": "UCsT0YIqwnpJCM-mx7-gSA4Q",
                    "title": "Letting in the Light: Finding the Positive to Overcome Adversity  | Shereen Hamza | TEDxUAlberta",
                    "description": "Friends, colleagues and even acquaintances have long asked Dr. Hamza how she manages to be so optimistic. More recently ...",
                    "thumbnails": {
                        "default": {
                            "url": "https://i.ytimg.com/vi/nIu8GZH54OA/default.jpg",
                            "width": 120,
                            "height": 90
                        },
                        "medium": {
                            "url": "https://i.ytimg.com/vi/nIu8GZH54OA/mqdefault.jpg",
                            "width": 320,
                            "height": 180
                        },
                        "high": {
                            "url": "https://i.ytimg.com/vi/nIu8GZH54OA/hqdefault.jpg",
                            "width": 480,
                            "height": 360
                        }
                    },
                    "channelTitle": "TEDx Talks",
                    "liveBroadcastContent": "none",
                    "publishTime": "2022-07-25T16:50:50Z"
                }
            }
        ]
        topic = Topic.objects.create(
            topic="Overcoming Adversity",
            search_prompt="Overcoming Adversity",
        )
        self.assertEqual(topic.video_set.count(), 0)
        process_topic(topic)
        self.assertEqual(topic.video_set.count(), 2)
        video = topic.video_set.first()
