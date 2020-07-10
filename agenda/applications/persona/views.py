from django.shortcuts import render

from django.views.generic import ListView , TemplateView

# paquete para usar django rest framework e importar lista ListAPIView
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    # equivalente a DetailView
    RetrieveAPIView,
    # equivalente a DeleteView
    DestroyAPIView,
    UpdateAPIView,
    # recupera datos y los actualiza
    RetrieveUpdateAPIView,

)

# se omporta el arhivo serializers
from .serializers import (
    PersonSerializer,
    PersonaSerializer,
    PersonaSerializer2,
    ReunionSerializer,
    PersonaSerializer3,
    ReunionSerializer2,
    ReunionSerializerLink,
    PersonaPagination,
    CountReunionSerializer
)

from .models import Person, Reunion

class ListaPersonas(ListView):    
    template_name = "persona/personas.html"
    context_object_name = 'personas'
    
    def get_queryset(self):
        return Person.objects.all()
    
  # para rest   
class PersonListAPIView(ListAPIView): 
    # serializador que va a mostrar el resultado
    serializer_class = PersonSerializer
    
    def get_queryset(self):
        return Person.objects.all()
    
    
class PersonListView(TemplateView):
     template_name = "persona/lista.html"
          

class PersonSearchApiView(ListAPIView): 
    # serializador que va a mostrar el resultado
    serializer_class = PersonSerializer
    
    def get_queryset(self):
        # filtramos datos
        kword = self.kwargs['kword']
        return Person.objects.filter(
            full_name__icontains=kword
        )


class PersonaCreateView(CreateAPIView):
    serializer_class = PersonSerializer
    
class PersonaDetailView(RetrieveAPIView):
    serializer_class = PersonSerializer
    
    # necesita del parametro queryset
    # igual se necesita esto aunque el el PersonaSerializers se indique el model
    queryset = Person.objects.all()
        

class PersonaDeleteView(DestroyAPIView):
    serializer_class = PersonSerializer    
    queryset = Person.objects.all()
    
class PersonaUpdateView(UpdateAPIView):
    serializer_class = PersonSerializer    
    queryset = Person.objects.all()
    
class PersonaRetrieveUpdateView(RetrieveUpdateAPIView):
    serializer_class = PersonSerializer    
    queryset = Person.objects.all()
    
  
class PersonApiLista(ListAPIView):
  
    serializer_class = PersonaSerializer
    
    def get_queryset(self):
        return Person.objects.all()
    
  
class PersonApiLista2(ListAPIView):
  
    serializer_class = PersonaSerializer2
    
    def get_queryset(self):
        return Person.objects.all()
    
class ReunionApiLista(ListAPIView):
      
    serializer_class = ReunionSerializer
    
    def get_queryset(self):
        return Reunion.objects.all()

class PersonApiLista3(ListAPIView):
      
    serializer_class = PersonaSerializer3
    
    def get_queryset(self):
        return Person.objects.all()
    
class ReunionApiLista2(ListAPIView):
      
    serializer_class = ReunionSerializer2
    
    def get_queryset(self):
        return Reunion.objects.all()
    
class ReunionApiListaLink(ListAPIView):
      
    serializer_class = ReunionSerializerLink
    
    def get_queryset(self):
        return Reunion.objects.all()
    
# para lista personas con paginacion
class PersonPaginationList(ListAPIView):
      
    serializer_class = PersonaSerializer
    # PersonaPagination es un serializador
    pagination_class = PersonaPagination
    
    def get_queryset(self):
        return Person.objects.all()
    
class ReunionByPersonJob(ListAPIView):
    
    serializer_class = CountReunionSerializer

    def get_queryset(self):
        return Reunion.objects.cantidad_reuniones_job()
    
