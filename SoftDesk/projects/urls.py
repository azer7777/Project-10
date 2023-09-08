from django.urls import path, include
from rest_framework_nested import routers
from .views import ProjectViewSet, IssueViewSet, CommentViewSet

router = routers.DefaultRouter()
router.register(r"projects", ProjectViewSet)


issues_router = routers.NestedDefaultRouter(router, r"projects", lookup="project")
issues_router.register(r"issues", IssueViewSet, basename="project-issues")


comments_router = routers.NestedDefaultRouter(issues_router, r"issues", lookup="issue")
comments_router.register(r"comments", CommentViewSet, basename="issue-comments")

urlpatterns = [
    path("", include(router.urls)),
    path("", include(issues_router.urls)),
    path("", include(comments_router.urls)),
]
