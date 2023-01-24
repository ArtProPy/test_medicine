from datetime import datetime

from django.db.models import Max
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.mixins import ListModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from medicine.models import Reference, ElementReference
from medicine import serializers

mapper = {
    'reference': {
        'list': serializers.ReferencesSerializer,
        'id': serializers.ReferencesIdSerializer,
        'name': serializers.ReferencesNameSerializer,
    },
    'elementreference': {
        'list': serializers.ElementReferenceSerializer,
        'code': serializers.ElementReferenceCodeSerializer,
        'value': serializers.ElementReferenceValueSerializer,
    }
}


class BaseApi(ListModelMixin, GenericViewSet):
    filterset_fields = '__all__'
    content = ''

    def get_serializer_class(self):
        dict_serializers = mapper.get(self.queryset.model._meta.model_name, {})
        return dict_serializers.get(self.kwargs.get('field', self.action), self.serializer_class)

    def list(self, request, *args, **kwargs):
        query = super().list(request, *args, **kwargs)
        query.data = {self.content: query.data}
        return query


class ReferenceViewSet(BaseApi):
    serializer_class = serializers.ReferencesSerializer
    queryset = Reference.objects.all()
    content = 'refbooks'

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.query_params.get('date'):
            queryset = queryset.filter(
                versions_reference__date__lte=self.request.query_params.get('date')
            )
        return queryset

    @swagger_auto_schema(
        operation_summary='Получить список справочников',
        operation_description='Получает список справочников',
        tags=['Справочник'],
        manual_parameters=[openapi.Parameter('date', in_=openapi.IN_QUERY,
                           type=openapi.TYPE_STRING, format='YYYY-mm-dd')]
    )
    def refbooks(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary='Получить список id справочников',
        operation_description='Получает список идентификаторов справочников справочников',
        tags=['Справочник'],
        manual_parameters=[openapi.Parameter('date', in_=openapi.IN_QUERY,
                           type=openapi.TYPE_STRING, format='YYYY-mm-dd')]
    )
    def refbooks_id(self, request, *args, **kwargs):
        return self.refbooks(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary='Получить список названий справочников',
        operation_description='Получает список названий справочников',
        tags=['Справочник'],
        manual_parameters=[openapi.Parameter('date', in_=openapi.IN_QUERY,
                           type=openapi.TYPE_STRING, format='YYYY-mm-dd')]
    )
    def refbooks_name(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class ElementReferenceViewSet(BaseApi):
    serializer_class = serializers.ElementReferenceSerializer
    queryset = ElementReference.objects.all()
    content = 'elements'

    def get_queryset(self):
        queryset = super().get_queryset().filter(version_reference__reference_id=self.kwargs['id'])
        if self.request.query_params.get('version'):
            queryset = queryset.filter(version_reference__version=self.request.query_params['version'])
        else:
            currect_date = queryset.filter(
                version_reference__date__lte=datetime.now()
            ).aggregate(
                date=Max('version_reference__date')
            )['date']
            queryset = queryset.filter(version_reference__date=currect_date)

        return queryset

    @swagger_auto_schema(
        operation_summary='Получить список элементов справочника',
        operation_description='Получает список элементов справочника',
        tags=['Элементы справочника'],
        manual_parameters=[openapi.Parameter('version', in_=openapi.IN_QUERY,
                           type=openapi.TYPE_STRING)]
    )
    def refbooks_elements(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary='Получить список id элементов справочника',
        operation_description='Получает список идентификаторов элементов справочника',
        tags=['Элементы справочника'],
        manual_parameters=[openapi.Parameter('version', in_=openapi.IN_QUERY,
                           type=openapi.TYPE_STRING)]
    )
    def refbooks_elements_id(self, request, *args, **kwargs):
        return self.refbooks_elements(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary='Получить список названий элементов справочника',
        operation_description='Получает список названий элементов справочника',
        tags=['Элементы справочника'],
        manual_parameters=[openapi.Parameter('version', in_=openapi.IN_QUERY,
                           type=openapi.TYPE_STRING)]
    )
    def refbooks_elements_name(self, request, *args, **kwargs):
        return self.refbooks_elements(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary='Ищет элемент справочника, соответствующий коду и значению',
        operation_description='Определяет, есть ли у указанного справочника элемент с указанными '
                              'кодом и значением (в указанной версии)',
        tags=['Элементы справочника'],
        responses={401: 'Указаны не все необходиммые данные'}
    )
    def check_element(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        if self.request.query_params.get('version'):
            queryset = queryset.filter(version_reference__version=self.request.query_params['version'])
        if not self.request.query_params.get('code'):
            return Response('Не указан код элемента', status=status.HTTP_400_BAD_REQUEST)
        if not self.request.query_params.get('value'):
            return Response('Не указано значение элемента', status=status.HTTP_400_BAD_REQUEST)
        queryset = queryset.filter(code=self.request.query_params['code'], value=self.request.query_params['value'])
        return Response(bool(queryset))
