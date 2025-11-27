from django.urls import path
from .views import RegisterUserView

#USer End points
app_name = "accounts"

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register'),
    # login is via JWT token endpoint at the project level (/api/token/)
]
