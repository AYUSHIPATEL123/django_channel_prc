"""
ASGI config for core project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/
"""
import os
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
from django.urls import path, re_path
from app.consumers import TestClass

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

application = get_asgi_application()

asgi_patterns = [
    path('ws/test/', TestClass.as_asgi()),
]

application = ProtocolTypeRouter({
    "http": application,
    "websocket": URLRouter(asgi_patterns)
})