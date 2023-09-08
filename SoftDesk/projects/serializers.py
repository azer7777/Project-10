from rest_framework import serializers
from .models import Project, Issue, Comment
from accounts.models import CustomUser


class BaseResourceSerializer(serializers.ModelSerializer):
    created_time = serializers.DateTimeField(read_only=True)
    author = serializers.ReadOnlyField(source='author.username')


class CommentSerializer(BaseResourceSerializer):
    issues = serializers.PrimaryKeyRelatedField(queryset=Issue.objects.all(), required=False)
    class Meta:
        model = Comment
        fields = '__all__'

class IssueSerializer(BaseResourceSerializer):
    project = serializers.PrimaryKeyRelatedField(queryset=Project.objects.all(), required=False)
    comments = CommentSerializer(many=True, read_only=True)
    contributors = serializers.PrimaryKeyRelatedField(many=True, queryset=CustomUser.objects.all(), required=False)
    assignee = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all(), required=False)
    
    class Meta:
        model = Issue
        fields = '__all__'

class ProjectSerializer(BaseResourceSerializer):
    issue_ids = serializers.PrimaryKeyRelatedField(many=True, read_only=True, source='issues')
    contributors = serializers.PrimaryKeyRelatedField(many=True, queryset=CustomUser.objects.all(), required=False)


    class Meta:
        model = Project
        fields = '__all__'
