from api.models import *
from rest_framework import serializers

class GuitarSerializer(serializers.ModelSerializer):
    #member = serializers.SlugRelatedField(queryset = BandMember.objects.all(), slug_field='id')
    class Meta:
        model = Guitar
        fields = ('name','member')
        depth = 1

class BandMemberSerializer(serializers.ModelSerializer):
    guitars = GuitarSerializer(many=True)
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


