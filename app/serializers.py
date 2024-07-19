from rest_framework import serializers

from app.models import Agents


class AgentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agents
        fields = '__all__'
