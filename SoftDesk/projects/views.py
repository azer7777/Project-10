from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Project, Issue, Comment
from .serializers import ProjectSerializer, IssueSerializer, CommentSerializer
from .permissions import IsAuthorOrReadOnly, IsContributor

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        user = self.request.user
        queryset = Project.objects.filter(contributors=user)
        return queryset

    def perform_create(self, serializer):
        author = self.request.user
        contributors = [author]
        contributors_data = self.request.data.get('contributors', [])  # Get the contributors from the request data
        contributors.extend(contributors_data)  # Extend the list with contributors from the request
        serializer.save(author=author, contributors=contributors)
        
    @action(detail=True, methods=['GET'])
    def issues(self, request, pk=None):
        project = self.get_object()
        issues = project.issues.all()
        serializer = IssueSerializer(issues, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['GET'])
    def comments(self, request, pk=None):
        project = self.get_object()
        comments = project.comments.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)   
    
    


