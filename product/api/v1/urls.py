from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.v1.views.course_view import CourseViewSet, GroupViewSet, LessonViewSet
from api.v1.views.user_view import UserViewSet

v1_router = DefaultRouter()
v1_router.register('users', UserViewSet, basename='users')
v1_router.register('courses', CourseViewSet, basename='courses')
v1_router.register(
    r'courses/(?P<course_id>\d+)/lessons', LessonViewSet, basename='lessons'
)
v1_router.register(
    r'courses/(?P<course_id>\d+)/groups', GroupViewSet, basename='groups'
)

urlpatterns = [
    path("", include(v1_router.urls)),
    path("auth/", include('djoser.urls')),
    path("auth/", include('djoser.urls.authtoken')),
    # Создание нового пользователя api/v1/auth/users/
    # Авторизация пользователя     api/v1/auth/token/login/
]
