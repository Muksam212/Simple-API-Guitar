from api.models import *
from rest_framework import serializers

class GuitarSerializer(serializers.ModelSerializer):
    member = serializers.PrimaryKeyRelatedField(queryset=BandMember.objects.all(), many=False, read_only=False)
    class Meta:
        model = Guitar
        fields = ('name','member')
        depth = 1

class BandMemberSerializer(serializers.ModelSerializer):
    guitars = GuitarSerializer(many=True)
    band = serializers.PrimaryKeyRelatedField(queryset=Band.objects.all(), many=False, read_only=False)
    class Meta:
        model = BandMember
        fields = ('id','name','band','image','phone_number','email','guitars')
        depth = 1

class BandSerializer(serializers.ModelSerializer):
    band_members = BandMemberSerializer(many=True)
    class Meta:
        model = Band
        fields = ('id','name','logo','band_members')
        depth = 1


