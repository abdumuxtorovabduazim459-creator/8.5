from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Genre, Book
from .serializers import GenreSerializer, BookSerializer


class GenreViewSet(ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

    # GET /api/genres/<pk>/books/  -> shu janrdagi kitoblar
    @action(detail=True, methods=['get'])
    def books(self, request, pk=None):
        genre = self.get_object()
        books = Book.objects.select_related('genre').filter(genre=genre)
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)


class BookViewSet(ModelViewSet):
    queryset = Book.objects.select_related('genre')
    serializer_class = BookSerializer
