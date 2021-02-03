from django.shortcuts import render
from rest_framework.response import Response
from .models import Snippet,Author,Book
from .serializers import SnippetSerializer
from django.contrib.auth.models import User
from .serializers import UserSerializer,AuthorSerializer,BookSerializer
from rest_framework import permissions
from .permissions import IsOwnerOrReadOnly
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework import renderers
from rest_framework import viewsets
from rest_framework.decorators import action
# REST framework provides two wrappers you can use to write API views.

# The @api_view decorator for working with function based views.
# The APIView class for working with class-based views.

# To handle URLs like this: http://example.com/api/items/4.json.

# Create your views here.
class SnippetViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

class AuthorViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class BookViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def create(self, request, *args, **kwargs):
        author  = Author.objects.get(id=request.data.get('author'))
        author = AuthorSerializer(author)
        request._full_data.update({'author':author.data})
        return super().create(request, *args, **kwargs)


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'snippets': reverse('snippet-list', request=request, format=format)
    })
    