
from rest_framework.generics import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from api.models import *
from api.serializers import BandSerializer, BandMemberSerializer, GuitarSerializer

import uuid

# Create your views here.
class BandCreate(CreateAPIView):
    serializer_class = BandSerializer
    queryset = Band.objects.all()

class BandList(APIView):
    def get(self, request, format=None):
        band = Band.objects.all()
        serializer = BandSerializer(band, many=True)
        return Response(serializer.data)

class BandUpdate(UpdateAPIView):
    serializer_class = BandSerializer
    queryset = Band.objects.all()
    lookup_field = 'id'

class BandDelete(APIView):
    def delete(self, request, id):
        band = Band.objects.get(id=id)
        band.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class BandMemberCreate(CreateAPIView):
    serializer_class = BandMemberSerializer
    queryset = BandMember.objects.all()
    permission_classes = [IsAuthenticated]

class BandMemberList(ListAPIView):
    serializer_class = BandMemberSerializer
    queryset = BandMember.objects.all()
    permission_classes = [IsAuthenticated]

class BandMemberUpdate(UpdateAPIView):
    serializer_class = BandMemberSerializer
    queryset = BandMember.objects.all()
    permission_classes = [IsAuthenticated]
    lookup_field = "id"

class BandMemberDelete(APIView):
    permission_classes = [IsAuthenticated]
    def delete(self, request, id):
        band_member = BandMember.objects.get(id=id)
        band_member.delete()
        return Response(status=status.HTTP_404_NOT_FOUND)


class GuitarCreate(CreateAPIView):
    serializer_class = GuitarSerializer
    queryset = Guitar.objects.all()


class GuitarList(ListAPIView):
    serializer_class = GuitarSerializer
    queryset = Guitar.objects.all()