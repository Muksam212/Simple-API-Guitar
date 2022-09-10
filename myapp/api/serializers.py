from api.models import *
from rest_framework import serializers

class GuitarSerializer(serializers.ModelSerializer):
    #member = serializers.SlugRelatedField(queryset = BandMember.objects.all(), slug_field='id')
    class Meta:
        model = Guitar
        fields = ('name','member')
        depth = 1


# class BandMemberRegistration(serializers.ModelSerializer):
#     username = serializers.CharField(max_length=100)
#     email = serializers.EmailField(max_length=100)
#     password = serializers.CharField(max_length=100, write_only=True)
    
#     class Meta:
#         model = BandMember
#         fields = ('username','email','password')

#     def validate(self, args):
#         username = args.get('username')
#         email = args.get('email')

#         if BandMember.objects.filter(username=username).exists():
#             raise serializers.ValidationError("Username already exists")
#         elif BandMember.objects.filter(email=email).exists():
#             raise serializers.ValidationError("Email already exists")
#         return super().validate(args)

#     def create(self,validated_data):
#         return BandMember.objects.create_user(**validated_data)

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


