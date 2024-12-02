from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Azkar, DatabaseVersion
from .serializers import AzkarSerializer, DatabaseVersionSerializer

class AzkarViewSet(ModelViewSet):
    queryset = Azkar.objects.all()
    serializer_class = AzkarSerializer

class DatabaseVersionView(APIView):
    def get(self, request):
        db_version = DatabaseVersion.objects.last()
        if db_version:
            serializer = DatabaseVersionSerializer(db_version)
            return Response(serializer.data)
        return Response({"error": "No version found"}, status=404)

