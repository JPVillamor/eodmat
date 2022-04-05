from django.urls import path
import django
django.setup()
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from .consumers import WSConsumer

ws_urlpatterns = [
    path('ws/matserver/', WSConsumer.as_asgi())
]

application = ProtocolTypeRouter({
    'websocket':AuthMiddlewareStack(URLRouter(ws_urlpatterns))
})
