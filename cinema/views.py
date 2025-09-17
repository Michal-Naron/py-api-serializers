from rest_framework.viewsets import ModelViewSet

from cinema.serializers import (
    GenreSerializer,
    ActorSerializer,
    CinemaHallSerializer,
    MovieSerializer,
    MovieSessionSerializer,
    MovieSessionRetrieveListSerializer,
    MovieListSerializer,
    MovieRetrieveSerializer
)
from cinema.models import (
    Genre,
    Actor,
    CinemaHall,
    Movie,
    MovieSession
)

class GenreViewSet(ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class ActorViewSet(ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class CinemaHallViewSet(ModelViewSet):
    queryset = CinemaHall.objects.all()
    serializer_class = CinemaHallSerializer


class MovieViewSet(ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def get_serializer_class(self):
        if self.action == "list":
            return MovieListSerializer
        elif self.action == "retrieve":
            return  MovieRetrieveSerializer
        return self.serializer_class

    def get_queryset(self):
        if self.action == "list":
            return Movie.objects.all().select_related()
        return self.queryset




class MovieSessionViewSet(ModelViewSet):
    queryset = MovieSession.objects.all()
    serializer_class = MovieSessionSerializer

    def get_serializer_class(self):
        if self.action in ("list", "retrieve"):
            return  MovieSessionRetrieveListSerializer
        return self.serializer_class

    def get_queryset(self):
        if self.action == "list":
            return MovieSession.objects.all().select_related()
        return self.queryset