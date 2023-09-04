from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Project, Issue, Comment
from .serializers import ProjectSerializer, IssueSerializer, CommentSerializer
from .permissions import IsAuthorOrReadOnly, IsContributor

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly, IsContributor]
    
    def get_queryset(self):
        # Get the current user
        user = self.request.user

        # Filter projects where the user is a contributor
        queryset = Project.objects.filter(contributors=user)

        return queryset

    def perform_create(self, serializer):
        author = self.request.user
        contributors = [author]
        contributors_data = self.request.data.get('contributors', [])  # Get the contributors from the request data
        contributors.extend(contributors_data)  # Extend the list with contributors from the request
        serializer.save(author=author, contributors=contributors)


class IssueViewSet(viewsets.ModelViewSet):
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly, IsContributor]



class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
