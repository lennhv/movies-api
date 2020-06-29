from rest_framework import pagination
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import (
    ListCreateAPIView, RetrieveUpdateDestroyAPIView,
    RetrieveUpdateAPIView, DestroyAPIView,)


from .serializers import (
    MovieSerializer, MovieDetailSerializer, MovieDirectorsSerializer,
    MovieProducersSerializer, MovieCastingSerializer,
    PersonSerializer, PersonDetailSerializer,
    PersonAliasSerializer, PersonAsDirectorSerializer,
    PersonAsProducerSerializer, PersonAsCastingSerializer)

from .models import Movie, Person


class MovieCreateApiView(ListCreateAPIView):
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()
    lookup_field = "id"

class MovieDetailApiView(RetrieveUpdateDestroyAPIView):
    serializer_class = MovieDetailSerializer
    queryset = Movie.objects.all()
    lookup_field = "id"


class MovieDirectorsApiView(RetrieveUpdateAPIView):
    serializer_class = MovieDirectorsSerializer
    queryset = Movie.objects.all()
    lookup_field = "id"

class MovieDeleteDirectorsApiView(DestroyAPIView):
    queryset = Movie.objects.all()
    lookup_field = "id"

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        Movie.objects.del_director(instance, kwargs)
        return Response(status=status.HTTP_204_NO_CONTENT)


class MovieProducersApiView(RetrieveUpdateAPIView):
    serializer_class = MovieProducersSerializer
    queryset = Movie.objects.all()
    lookup_field = "id"

class MovieDeleteProducersApiView(DestroyAPIView):
    queryset = Movie.objects.all()
    lookup_field = "id"

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        Movie.objects.del_producer(instance, kwargs)
        return Response(status=status.HTTP_204_NO_CONTENT)


class MovieCastingApiView(RetrieveUpdateAPIView):
    serializer_class = MovieCastingSerializer
    queryset = Movie.objects.all()
    lookup_field = "id"

class MovieDeleteCastingApiView(DestroyAPIView):
    queryset = Movie.objects.all()
    lookup_field = "id"

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        Movie.objects.del_casting(instance, kwargs)
        return Response(status=status.HTTP_204_NO_CONTENT)




class PersonCreateApiView(ListCreateAPIView):
    serializer_class = PersonSerializer
    queryset = Person.objects.all()
    lookup_field = "id"

class PersonDetailApiView(RetrieveUpdateDestroyAPIView):
    serializer_class = PersonDetailSerializer
    queryset = Person.objects.all()
    lookup_field = "id"


class PersonAliasApiView(RetrieveUpdateAPIView):
    """ List all Person aliasses or create a new alias
    """
    serializer_class = PersonAliasSerializer
    queryset = Person.objects.all()
    lookup_field = "id"

class PersonAliasDeleteApiView(DestroyAPIView):
    """ Delete an especific alias by alias name
    """
    # serializer_class = PersonAliasSerializer
    queryset = Person.objects.all()
    lookup_field = "id"

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        Person.objects.del_alias(instance, kwargs)
        return Response(status=status.HTTP_204_NO_CONTENT)


class PersonAsDirectorApiView(RetrieveUpdateAPIView):
    """ 
    """
    serializer_class = PersonAsDirectorSerializer
    queryset = Person.objects.all()
    lookup_field = "id"

class PersonAsDirectorDeleteApiView(DestroyAPIView):
    """ 
    """
    # serializer_class = PersonAliasSerializer
    queryset = Person.objects.all()
    lookup_field = "id"

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        Person.objects.del_directed_movie(instance, kwargs)
        return Response(status=status.HTTP_204_NO_CONTENT)


class PersonAsProducerApiView(RetrieveUpdateAPIView):
    """ 
    """
    serializer_class = PersonAsProducerSerializer
    queryset = Person.objects.all()
    lookup_field = "id"

class PersonAsProducerDeleteApiView(DestroyAPIView):
    """ 
    """
    queryset = Person.objects.all()
    lookup_field = "id"

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        Person.objects.del_producted_movie(instance, kwargs)
        return Response(status=status.HTTP_204_NO_CONTENT)


class PersonAsCastingApiView(RetrieveUpdateAPIView):
    """ 
    """
    serializer_class = PersonAsCastingSerializer
    queryset = Person.objects.all()
    lookup_field = "id"

class PersonAsCastingDeleteApiView(DestroyAPIView):
    """ 
    """
    queryset = Person.objects.all()
    lookup_field = "id"

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        Person.objects.del_casted_movie(instance, kwargs)
        return Response(status=status.HTTP_204_NO_CONTENT)
