from rest_framework import serializers
from .models import Project, Issue, Comment
class CommentSerializer(serializers.ModelSerializer):
    created_time = serializers.DateTimeField(read_only=True)
    
    class Meta:
        model = Comment
        fields = '__all__'

class IssueSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    created_time = serializers.DateTimeField(read_only=True)
    
    class Meta:
        model = Issue
        fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):
    issues = IssueSerializer(many=True, read_only=True)
    created_time = serializers.DateTimeField(read_only=True)
    author = serializers.ReadOnlyField(source='author.username')
    contributors = serializers.PrimaryKeyRelatedField(many=True, read_only=True)


    class Meta:
        model = Project
        fields = '__all__'
