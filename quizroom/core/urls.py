from django.urls import path, include, re_path
from django.contrib.auth import views as auth_views
from allauth.account.urls import urlpatterns as allauth_urls
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="QuizRoom",
      default_version='v1',
      description="API documentation for QuizRoom",
      license=openapi.License(name="MIT License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    # Auth routes
    path('auth/login/', auth_views.LoginView.as_view(), name='login'),
    path('auth/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('auth/signup/', views.create_user, name='signup'),

    # Allauth routes
    path('accounts/', include(allauth_urls), name='accounts'),

    # JWT routes
    path('auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Swagger routes
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    # User routes
    path('users/', views.get_users, name='get_users'),
    path('users/<int:pk>/', views.get_user, name='get_user'),
    path('users/create/', views.create_user, name='create_user'),
    path('users/update/<int:pk>/', views.update_user, name='update_user'),
    path('users/delete/<int:pk>/', views.delete_user, name='delete_user'),

    # Room routes
    path('rooms/', views.get_rooms, name='get_rooms'),
    path('rooms/<int:pk>/', views.get_room, name='get_room'),
    path('rooms/create/', views.create_room, name='create_room'),
    path('rooms/update/<int:pk>/', views.update_room, name='update_room'),
    path('rooms/delete/<int:pk>/', views.delete_room, name='delete_room'),

    # Question routes
    path('questions/', views.get_questions, name='get_questions'),
    path('questions/<int:pk>/', views.get_question, name='get_question'),
    path('questions/create/', views.create_question, name='create_question'),
    path('questions/update/<int:pk>/', views.update_question, name='update_question'),
    path('questions/delete/<int:pk>/', views.delete_question, name='delete_question'),

    # Answer routes
    path('answers/', views.get_answers, name='get_answers'),
    path('answers/<int:pk>/', views.get_answer, name='get_answer'),
    path('answers/create/', views.create_answer, name='create_answer'),
    path('answers/update/<int:pk>/', views.update_answer, name='update_answer'),
    path('answers/delete/<int:pk>/', views.delete_answer, name='delete_answer'),
]