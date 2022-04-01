from rest_framework import generics, status
from rest_framework.response import Response
from .models import Empresa
from .serializers import EmpresaSerializer

class EmpresaDetalleView(generics.RetrieveAPIView):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

class EmpresasListaView(generics.ListAPIView):
    serializer_class = EmpresaSerializer
    queryset = Empresa.objects.all()
    def list(self, request):
        queryset = self.get_queryset()
        self.object_list = self.filter_queryset(queryset)
        convocatorias =  self.object_list
        serializer = EmpresaSerializer(convocatorias, many=True)
        return Response(serializer.data)


class EmpresaCrearView(generics.CreateAPIView):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer

    def post(self, request, *args, **kwargs):
        serializer = EmpresaSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response("Empresa creada", status=status.HTTP_200_OK)

class EmpresaEditarView(generics.UpdateAPIView):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer

    def put(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

class EmpresaEliminarView(generics.DestroyAPIView):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer

    def delete(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
