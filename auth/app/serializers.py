from rest_framework import serializers
from .models import Team, Person

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['id', 'name', 'members']

    members = serializers.StringRelatedField(many=True, read_only=True)

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ['id', 'first_name', 'last_name', 'email', 'team']
