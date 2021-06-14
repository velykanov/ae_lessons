from django.urls import path

from .views import FilmView

urlpatterns = [
    # path('index/', test_index),
    path('films/', FilmView.as_view()),
]
