from django.contrib import admin
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Topic(models.Model):
    """
    Model to store the topics and search prompts.
    The search process will search and save videos using all the search prompts here.
    """
    topic = models.TextField()
    search_prompt = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.topic


class Video(models.Model):
    """
    Model to store the video details, retrieved via a search using a topic.
    """
    videoId = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    description = models.TextField()
    channel_title = models.CharField(max_length=255)
    channel_id = models.CharField(max_length=255)
    published_at = models.DateTimeField()
    url = models.URLField()
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
