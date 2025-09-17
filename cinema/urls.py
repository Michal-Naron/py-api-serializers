from django.urls import path, include
from rest_framework.routers import DefaultRouter

from cinema.views import (GenreViewSet, ActorViewSet, CinemaHallViewSet,
                          MovieViewSet, MovieSessionViewSet)

router = DefaultRouter()
router.register(
    "Genres",
    GenreViewSet
)
router.register(
    "Actors",
    ActorViewSet
)
router.register(
    "CinemaHalls",
    CinemaHallViewSet
)
router.register(
    "Movie",
    MovieViewSet
)
router.register(
    "MovieSessions",
    MovieSessionViewSet
)

urlpatterns = [
    path("", include(router.urls))
]

app_name = "cinema"
