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
        user = self.request.user
        queryset = Project.objects.filter(contributors=user)
        return queryset

    def perform_create(self, serializer):
        author = self.request.user
        contributors = [author]
        contributors_data = self.request.data.get('contributors', [])  # Get the contributors from the request data
        contributors.extend(contributors_data)  # Extend the list with contributors from the request
        serializer.save(author=author, contributors=contributors)



class IssueViewSet(viewsets.ModelViewSet):
    serializer_class = IssueSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Filter issues based on the project
        project_id = self.kwargs['project_pk']
        return Issue.objects.filter(project_id=project_id)

    def perform_create(self, serializer):
        # Ensure the project is set based on the URL
        project_id = self.kwargs['project_pk']
        project = Project.objects.get(pk=project_id)
        serializer.save(project=project)

class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Filter comments based on the issue
        project_id = self.kwargs['project_pk']
        issue_id = self.kwargs['issue_pk']
        return Comment.objects.filter(issue__project_id=project_id, issue_id=issue_id)

    def perform_create(self, serializer):
        # Ensure the issue is set based on the URL
        project_id = self.kwargs['project_pk']
        issue_id = self.kwargs['issue_pk']
        issue = Issue.objects.get(project_id=project_id, pk=issue_id)
        serializer.save(issue=issue)

   


