from rest_framework import serializers
from django.contrib.auth import get_user_model
from musicapp.models import Artiste

class ArtisteSerializer(serializers.ModelSerializer):
    class Meta:
        model =Artiste
        fields = ['id', 'first_name', 'last_name', 'age']

