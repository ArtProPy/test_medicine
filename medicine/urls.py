from django.urls import path

from medicine.views import ReferenceViewSet, ElementReferenceViewSet

app_name = 'medicine'

urlpatterns = [
    path(
        'refbooks.id/',
        ReferenceViewSet.as_view({'get': 'list'}),
        {'field': 'id'},
        name='ids_refbooks'
    ),
    path(
        'refbooks.name/',
        ReferenceViewSet.as_view({'get': 'list'}),
        {'field': 'name'},
        name='names_refbooks'
    ),
    path(
        'refbooks/',
        ReferenceViewSet.as_view({'get': 'list'}),
        name='all_refbooks'
    ),


    path(
        'refbooks/<id>/elements.code/',
        ElementReferenceViewSet.as_view({'get': 'list'}),
        {'field': 'code'},
        name='codes_elements'
    ),
    path(
        'refbooks/<id>/elements.value/',
        ElementReferenceViewSet.as_view({'get': 'list'}),
        {'field': 'value'},
        name='values_elements'
    ),
    path(
        'refbooks/<id>/elements/',
        ElementReferenceViewSet.as_view({'get': 'list'}),
        name='all_elements'
    ),
    path(
        'refbooks/<id>/check_element',
        ElementReferenceViewSet.as_view({'get': 'check_element'}),
        name='all_elements'
    )
]
