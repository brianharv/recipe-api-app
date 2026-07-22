"""
URL mappings for the User API
"""

from django.urls import path

from user import views

app_name = "user"

# The name="create" value allows us to the use reverse('user:create')
urlpatterns = [
    path("create/", views.CreateUserView.as_view(), name="create"),
    path("token/", views.CreateTokenView.as_view(), name="token"),
]
