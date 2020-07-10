from django.contrib import admin
from django.urls import path, re_path

from . import  views

app_name = 'personas_app'

urlpatterns = [
    path('personas/',
        views.ListaPersonas.as_view(),
        name = 'personas'
    ),
    path('api/persona/lista/',
        views.PersonListAPIView.as_view()
    ),
    path('lista/',
        views.PersonListView.as_view(),
        name = 'lista'
    ),
    path(
        'api/persona/search/<kword>/',
        views.PersonSearchApiView.as_view(),
    ),
    path(
        'api/persona/create/',
        views.PersonaCreateView.as_view(),
    ),
    path(
        'api/persona/detail/<pk>',
        views.PersonaDetailView.as_view(),
        name = 'detalle'
    ),
    path(
        'api/persona/delete/<pk>',
        views.PersonaDeleteView.as_view(),
    ),
    path(
        'api/persona/update/<pk>',
        views.PersonaUpdateView.as_view(),
    ),
    path(
        'api/persona/modificar/<pk>',
        views.PersonaRetrieveUpdateView.as_view(),
    ),
    path(
        'api/personas/',
        views.PersonApiLista.as_view(),
    ),
    path(
        'api/personas2/',
        views.PersonApiLista2.as_view(),
    ),
    path(
        'api/reuniones/',
        views.ReunionApiLista.as_view(),
    ),
    path(
        'api/personas3/',
        views.PersonApiLista3.as_view(),
    ),
    path(
        'api/reuniones2/',
        views.ReunionApiLista2.as_view(),
    ),
    path(
        'api/reuniones-link/',
        views.ReunionApiListaLink.as_view(),
    ),
    path(
        'api/personas/paginacion/',
        views.PersonPaginationList.as_view(),
    ),
    path(
        'api/reunion/por-job/',
        views.ReunionByPersonJob.as_view(),
    ),
]

