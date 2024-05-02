from celery import shared_task
from videos.models import Topic
from videos.scraper import process_topic


@shared_task()
def save_topic_videos(topic_id):
    topic = Topic.objects.get(id=topic_id)
    process_topic(topic)

