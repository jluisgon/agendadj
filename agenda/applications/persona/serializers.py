
# paquetes de serializadores

from rest_framework import serializers, pagination

from .models import Person, Reunion, Hobby

class PersonSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Person
        # se va el queryset se va a transformar de esta forma
        fields = ('__all__')


class PersonaSerializer(serializers.Serializer):
    # construye manualmente
    id = serializers.IntegerField()
    full_name = serializers.CharField()
    job = serializers.CharField()
    email = serializers.EmailField()
    phone = serializers.CharField()
    # para campos que no estan en el modelo y asi no da error al usar el Rest
    # establece un default
    activo = serializers.BooleanField(default = False)
    #  para campos que no estan en el modelo y asi no da error al usar el Rest
    # atributo no obligatorio para los modelo, el que lo tenga obtendra ese atributo
    activo1 = serializers.BooleanField(required = False)


class PersonaSerializer2(serializers.ModelSerializer):
    # se agrega un atributo que no esta en el modelo
    activo = serializers.BooleanField(default = False)
    
    class Meta:
        model = Person       
        fields = ('__all__')
    
class ReunionSerializer(serializers.ModelSerializer):  
    
    persona = PersonSerializer()
    
    class Meta:
        model = Reunion       
        fields = (
            'id',
            'fecha',
            'hora',
            'asunto',
            'persona'
        )
        
class HobbySerializer2(serializers.ModelSerializer):
    
       class Meta:
        model = Hobby       
        fields = ('__all__')
        
class PersonaSerializer3(serializers.ModelSerializer):
    
    hobbies = HobbySerializer2(many = True)
    
    class Meta:
        model = Person       
        fields = (
            'id',
            'full_name',
            'job',
            'email',
            'phone',
            'hobbies',
            'created'
        )     
            
class ReunionSerializer2(serializers.ModelSerializer):  
    # se va a procesar este metodo para llenar ese campo
    fecha_hora = serializers.SerializerMethodField()
       
    class Meta:
        model = Reunion       
        fields = (
            'id',
            'fecha',
            'hora',
            'asunto',
            'persona',
            # al colocarlo como SerializerMethodField se debe agregar aca
            'fecha_hora'
        )
        
    # el obj es el registro que se esta iterando
    def get_fecha_hora(self, obj):
        return str(obj.fecha) + '-' + str(obj.hora)
    
class ReunionSerializerLink(serializers.HyperlinkedModelSerializer):  
       
    class Meta:
        model = Reunion       
        fields = (
            'id',
            'fecha',
            'hora',
            'asunto',
            'persona'
        )
        # le indica que el modelo lleva foranea debe cargar como un link
        extra_kwargs = {
            # que aributo sea un link
            'persona' : {'view_name':'personas_app:detalle', 'lookup_field': 'pk'}
        }
        

class PersonaPagination (pagination.PageNumberPagination):
    # definir como ser la estructura de la paginazacion
    # tamano del bloque de pagina
    page_size = 5
    # tamano maximo que carge en memoria
    # estos 100 los divide entre 5 y asi va enviando la informacion
    max_page_size = 100
          

class CountReunionSerializer(serializers.Serializer):
    persona__job = serializers.CharField()
    cantidad = serializers.IntegerField()
        
        
    
    