from django.db.models.signals import post_save
from django.dispatch import receiver
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from django.template.loader import render_to_string
from .models import PostModel, UserModel, AdminModel


@receiver(post_save, sender=PostModel)
def handle_new_post(sender, instance, created, **kwargs):
    if not created:
        return

    channel_layer = get_channel_layer()
    user_name = instance.user.FirstName
    message = f"📢 {user_name} posted something new!"

    # 1. Notify all users
    async_to_sync(channel_layer.group_send)(
        "all_users",
        {
            "type": "send_notification",
            "message": message
        }
    )

    # 2. Notify all admins
    async_to_sync(channel_layer.group_send)(
        "all_admins",
        {
            "type": "send_notification",
            "message": message
        }
    )

    # 3. Send new post to all feed users
    post_html = f'''
    <div class="feed-card">
      <div class="post-header">
        <img src="https://i.pravatar.cc/45?u={instance.user.EmailId}" alt="User">
        <div>
          <strong>{instance.user.FirstName}</strong><br>
          <small>just now</small>
        </div>
      </div>
      <div class="mt-3">
        <p>{instance.content}</p>
        {"<img src='" + instance.image.url + "' class='img-fluid rounded'>" if instance.image else ""}
      </div>
      <div class="post-actions">
        <button>👍 Like</button>
        <button>💬 Comment</button>
        <button>↗️ Share</button>
      </div>
    </div>
    '''
    async_to_sync(channel_layer.group_send)(
        "feed_group",
        {
            "type": "send_new_post",
            "post_html": post_html,
        }
    )

    # 4. Refresh admin dashboard
    send_admin_dashboard_refresh()


def send_admin_dashboard_refresh():
    context = {
        'total_users': UserModel.objects.count(),
        'total_posts': PostModel.objects.count(),
        'online_admins': AdminModel.objects.count(),
        'recent_posts': PostModel.objects.order_by('-created_at')[:5],
    }

    # ✅ Use a partial template instead of full HTML layout
    dashboard_html = render_to_string("admin_dashboard_partial.html", context)

    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        "admin_group",
        {
            "type": "refresh_admin_dashboard",
            "dashboard_html": dashboard_html
        }
    )


@receiver(post_save, sender=UserModel)
@receiver(post_save, sender=AdminModel)
def refresh_dashboard_on_user_or_admin_change(sender, instance, created, **kwargs):
    send_admin_dashboard_refresh()
