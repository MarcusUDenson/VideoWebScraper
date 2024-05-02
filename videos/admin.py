from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Topic, Video
from .tasks import save_topic_videos

admin.site.register(User, UserAdmin)


class VideoInline(admin.TabularInline):
    model = Video


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):

    actions = ["retrieve_videos"]
    inlines = [VideoInline]

    @admin.action(description="Retrieve videos for the selected topics")
    def retrieve_videos(self, request, queryset):
        for topic in queryset:
            save_topic_videos.delay(topic.id)


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ["videoId", "title", "url", "topic"]
    search_fields = ["topic__topic", "title"]
    ordering = ["topic__id", "id"]
