from rest_framework import serializers
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet
from rest_framework import routers
from FileServer import settings
from server.models import FileServer


class FileServerSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileServer
        fields = '__all__'


class FileServerViewSet(ModelViewSet):
    permission_classes = [AllowAny]
    queryset = FileServer.objects.all()
    serializer_class = FileServerSerializer


if settings.DEBUG:
    router = routers.DefaultRouter()
else:
    router = routers.SimpleRouter()

router.register(r'files', FileServerViewSet)
