from django.urls import path
from projects.views import view_projects


urlpatterns = [
    path("", view_projects, name="view_projects"),
]
