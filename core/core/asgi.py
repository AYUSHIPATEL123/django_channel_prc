"""
ASGI config for core project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/
"""

import os
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from djnago.urls import path

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

asgi_patterns = [
    path('ws/some_path/', SomeConsumer.as_asgi()),
]
application = get_asgi_application()
application = ProtocolTypeRouter({
    "websocket": URLRouter(asgi_patterns),
})
