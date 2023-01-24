from rest_framework import serializers
from .models import Participant, Supplier


class ParticipantCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Participant
        read_only_fields = ('id', 'created')
        fields = '__all__'


class ParticipantSerializer(serializers.ModelSerializer):

    class Meta:
        model = Participant
        read_only_fields = ('id', 'created')
        fields = '__all__'


class SupplierCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Supplier
        read_only_fields = ('id', 'debt')
        fields = '__all__'


class SupplierSerializer(serializers.ModelSerializer):

    class Meta:
        model = Supplier
        read_only_fields = ('id', 'debt')
        fields = '__all__'
