from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/home/$', consumers.FeedConsumer.as_asgi()),               # for main.html
    re_path(r'ws/dashboard/$', consumers.AdminDashboardConsumer.as_asgi()), # for admin.html
    re_path(r'ws/notifications/$', consumers.NotificationConsumer.as_asgi()) # shared by both
]