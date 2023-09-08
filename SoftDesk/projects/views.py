from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Project, Issue, Comment
from .serializers import ProjectSerializer, IssueSerializer, CommentSerializer
from .permissions import IsAuthorOrReadOnly, IsContributor, CanAccessProjectResources
from django.db.models import Q


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly, IsContributor]

    def get_queryset(self):
        user = self.request.user
        queryset = Project.objects.filter(Q(contributors=user) | Q(author=user))
        return queryset

    def perform_create(self, serializer):
        author = self.request.user
        contributors = [author]
        contributors_data = self.request.data.get("contributors", [])
        contributors.extend(contributors_data)
        serializer.save(author=author, contributors=contributors)


class IssueViewSet(viewsets.ModelViewSet):
    serializer_class = IssueSerializer
    permission_classes = [IsAuthenticated, CanAccessProjectResources, IsAuthorOrReadOnly]

    def get_queryset(self):
        project_id = self.kwargs["project_pk"]
        return Issue.objects.filter(project_id=project_id)

    def perform_create(self, serializer):
        project_id = self.kwargs["project_pk"]
        project = Project.objects.get(pk=project_id)
        author = self.request.user
        serializer.save(project=project, author=author)

    def get_project_from_request(self, request):
        project_id = self.kwargs.get("project_pk")
        if project_id is not None:
            try:
                return Project.objects.get(pk=project_id)
            except Project.DoesNotExist:
                return None
        return None


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, CanAccessProjectResources, IsAuthorOrReadOnly]

    def get_queryset(self):
        project_id = self.kwargs["project_pk"]
        issue_id = self.kwargs["issue_pk"]
        return Comment.objects.filter(issue__project_id=project_id, issue_id=issue_id)

    def perform_create(self, serializer):
        project_id = self.kwargs["project_pk"]
        issue_id = self.kwargs["issue_pk"]
        issue = Issue.objects.get(project_id=project_id, pk=issue_id)
        author = self.request.user
        serializer.save(issue=issue, author=author)

    def get_project_from_request(self, request):
        project_id = self.kwargs.get("project_pk")
        if project_id is not None:
            try:
                return Project.objects.get(pk=project_id)
            except Project.DoesNotExist:
                return None
        return None
