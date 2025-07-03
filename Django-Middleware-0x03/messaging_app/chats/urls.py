from django.urls import path, include
from rest_framework import routers
from rest_framework_nested.routers import NestedDefaultRouter
from .views import ConversationViewSet, MessageViewSet

router = routers.DefaultRouter()
router.register(r'conversations', ConversationViewSet, basename='conversation')
router.register(r'messages', MessageViewSet, basename='message')

nested_router = NestedDefaultRouter()
nested_router.register(r'conversations', ConversationViewSet, basename='conversation')
nested_router.register(r'messages', MessageViewSet, basename='message')

app_name = 'chats'

urlpatterns = [
    path('', include(router.urls)),
    path('nested/', include(nested_router.urls)),
]