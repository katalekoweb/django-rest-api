from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.BlogPostListCreate.as_view(), name='blogpost-view-create'),
    path('<int:pk>/', views.BlogPostRetrieveUpdateDestroy.as_view(), name='update-blogpost'),
]