from rest_framework import serializers

from medicine.models import *


class ReferencesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reference
        fields = ('id', 'name', 'code')


class ReferencesIdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reference
        fields = ('id',)


class ReferencesNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reference
        fields = ('name',)


class VersionReferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = VersionReference
        fields = '__all__'


class ElementReferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ElementReference
        fields = ('code', 'value')


class ElementReferenceCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ElementReference
        fields = ('code',)


class ElementReferenceValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = ElementReference
        fields = ('value',)
