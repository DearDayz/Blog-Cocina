
from rest_framework import generics
from .models import Receta
from .serializers import RecetaSerializer
from rest_framework import viewsets
from drf_spectacular.utils import extend_schema, OpenApiResponse, OpenApiExample
from .tablas import get_table, get_example, post_table, post_example


# Create your views here.
class RecetaAPIList(generics.ListAPIView):
    queryset = Receta.objects.all()



#ViewSets
class RecetaViewSet(viewsets.ModelViewSet):
    queryset = Receta.objects.all()
    serializer_class = RecetaSerializer

    @extend_schema(
        responses={
            200: OpenApiResponse(
                description=get_table,
                response=RecetaSerializer(many=True),  # Documentar usando el serializer asda
                examples=[
                    OpenApiExample(
                        'Real',
                        value=get_example)]
            ),
        },
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    

    @extend_schema(
        request=RecetaSerializer,  # Documentar el request usando el serializer
        responses={
            201: OpenApiResponse(
                description=post_table,
                response=RecetaSerializer(),
                examples=[
                    OpenApiExample(
                        'Ejemplo de cuerpo de solicitud',
                        value=[post_example]
                    )
                ]
            ),
            400: OpenApiResponse(
                description='Error de validación',
            ),
        },
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
