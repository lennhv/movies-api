from django.urls import path


from .api import (
    MovieCreateApiView, MovieDetailApiView, 
    MovieDirectorsApiView, MovieDeleteDirectorsApiView,
    MovieProducersApiView, MovieDeleteProducersApiView,
    MovieCastingApiView, MovieDeleteCastingApiView,
    PersonCreateApiView, PersonDetailApiView,
    PersonAliasApiView, PersonAliasDeleteApiView,
    PersonAsDirectorApiView, PersonAsDirectorDeleteApiView,
    PersonAsProducerApiView, PersonAsProducerDeleteApiView,
    PersonAsCastingApiView, PersonAsCastingDeleteApiView,)

from .views import home

urlpatterns = [
    path("", home, name='home'),
    path('movies/', MovieCreateApiView.as_view(), name='api-movies'),
    path('movies/<uuid:id>/', MovieDetailApiView.as_view(), name='api-movies-detail'),
    path('movies/<uuid:id>/directors/', MovieDirectorsApiView.as_view(), name='api-movies-directors'),
    path('movies/<uuid:id>/directors/<uuid:person_id>/', MovieDeleteDirectorsApiView.as_view(), name='api-movies-director-delete'),
    path('movies/<uuid:id>/producers/', MovieProducersApiView.as_view(), name='api-movies-producers'),
    path('movies/<uuid:id>/producers/<uuid:person_id>/', MovieDeleteProducersApiView.as_view(), name='api-movies-producer-delete'),
    path('movies/<uuid:id>/casting/', MovieCastingApiView.as_view(), name='api-movies-casting'),
    path('movies/<uuid:id>/casting/<uuid:person_id>/', MovieDeleteCastingApiView.as_view(), name='api-movies-casting-delete'),

    path('persons/', PersonCreateApiView.as_view(), name='api-persons'),
    path('persons/<uuid:id>/', PersonDetailApiView.as_view(), name='api-persons-detail'),
    path('persons/<uuid:id>/aliasses/', PersonAliasApiView.as_view(), name='api-persons-alias'),
    path('persons/<uuid:id>/aliasses/<str:name>/', PersonAliasDeleteApiView.as_view(), name='api-persons-alias-delete'),
    path('persons/<uuid:id>/moviesasdirector/', PersonAsDirectorApiView.as_view(), name='api-persons-director'),
    path('persons/<uuid:id>/moviesasdirector/<uuid:movie_id>/', PersonAsDirectorDeleteApiView.as_view(), name='api-persons-director-delete'),
    path('persons/<uuid:id>/moviesasproducer/', PersonAsProducerApiView.as_view(), name='api-persons-producer'),
    path('persons/<uuid:id>/moviesasproducer/<uuid:movie_id>/', PersonAsProducerDeleteApiView.as_view(), name='api-persons-producer-delete'),
    path('persons/<uuid:id>/moviesascasting/', PersonAsCastingApiView.as_view(), name='api-persons-producer'),
    path('persons/<uuid:id>/moviesascasting/<uuid:movie_id>/', PersonAsCastingDeleteApiView.as_view(), name='api-persons-producer-delete'),
]

