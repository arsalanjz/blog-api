from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permissions import IsAdminOrReadOnly, IsAuthorOrReadOnly
from .models import PostModel
from .serializers import PostSerializer
from django.contrib.postgres.search import TrigramSimilarity
from django.db.models.functions import Greatest


class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly , IsAdminOrReadOnly , IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_queryset(self):
        queryset = PostModel.objects.all().order_by('-created')
        search_query = self.request.query_params.get('search', None)
        if search_query:
            queryset = queryset.annotate(
                similarity=Greatest(
                    TrigramSimilarity('title', search_query),
                    TrigramSimilarity('content', search_query)
                )
            ).filter(similarity__gt=0.02).order_by('-similarity')
        return queryset


