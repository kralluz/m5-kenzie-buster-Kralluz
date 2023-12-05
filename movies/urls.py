from django.urls import path
from .views import MovieView

urlpatterns = [
    path('movies/', MovieView.as_view()),
    path('movies/<int:movie_id>/', MovieView.as_view())
    # path('movies?movie=title_name', MovieView.as_view())
]
