from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token
from cars import views

app_name = "cars"

urlpatterns = [
    path("cars/", views.CarsList.as_view(), name="cars-list"),
    path("cars/<int:pk>/", views.CarDetail.as_view(), name="car-detail"),
    path("users/", views.UsersList.as_view(), name="users-list"),
    path("users/<int:pk>/", views.UserDetail.as_view(), name="user-detail"),
    path('auth/obtain-jwt-token/', obtain_jwt_token, name="obtain-jwt-token"),
    path('auth/refresh-token/', refresh_jwt_token, name="refresh-token"),
    path('auth/verify-token/', verify_jwt_token, name="verify-token"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
