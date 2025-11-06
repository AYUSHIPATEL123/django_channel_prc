from django.db import models
from django.contrib.auth.models import User
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
import json
# Create your models here.
class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    notification=models.CharField(max_length=255)
    is_seen=models.BooleanField(default=False)
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        channel = get_channel_layer()
        data_object = Notification.objects.filter(is_seen=False).count()
        data = {
            "count":data_object,
            "notification":self.notification
        } 
        data = async_to_sync(channel.group_send)("test_group", {
            "type": "send_notification",
            "message": json.dumps(data)
            })
        
        