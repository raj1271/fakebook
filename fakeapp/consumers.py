import json
from channels.generic.websocket import AsyncWebsocketConsumer

class FeedConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add("feed_group", self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("feed_group", self.channel_name)

    async def send_new_post(self, event):
        await self.send(text_data=json.dumps({
            'type': 'new_post',
            'post_html': event['post_html']
        }))


class AdminDashboardConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add("admin_group", self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("admin_group", self.channel_name)

    async def refresh_admin_dashboard(self, event):
        await self.send(text_data=json.dumps({
            'type': 'dashboard_refresh',
            'dashboard_html': event['dashboard_html']
        }))


class NotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        session = self.scope['session']
        if session.get("user_emailId"):
            self.group_name = "all_users"
        elif session.get("adminemail"):
            self.group_name = "all_admins"
        else:
            await self.close()
            return

        await self.channel_layer.group_add(self.group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.group_name, self.channel_name)

    async def send_notification(self, event):
        await self.send(text_data=json.dumps({
            'type': 'notify',
            'message': event['message']
        }))


