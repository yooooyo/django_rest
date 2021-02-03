from django.urls import path,include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet)
router.register(r'books', views.BookViewSet)
router.register(r'authors', views.AuthorViewSet)
router.register(r'users', views.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

# urlpatterns = format_suffix_patterns(urlpatterns)