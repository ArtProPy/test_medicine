from django.urls import path

from medicine.views import ReferenceViewSet, ElementReferenceViewSet

app_name = 'medicine'

urlpatterns = [
    path(
        'refbooks.id/',
        ReferenceViewSet.as_view({'get': 'refbooks_id'}),
        {'field': 'id'},
        name='ids_refbooks'
    ),
    path(
        'refbooks.name/',
        ReferenceViewSet.as_view({'get': 'refbooks_name'}),
        {'field': 'name'},
        name='names_refbooks'
    ),
    path(
        'refbooks/',
        ReferenceViewSet.as_view({'get': 'refbooks'}),
        name='all_refbooks'
    ),


    path(
        'refbooks/<id>/elements.code/',
        ElementReferenceViewSet.as_view({'get': 'refbooks_elements'}),
        {'field': 'code'},
        name='codes_elements'
    ),
    path(
        'refbooks/<id>/elements.value/',
        ElementReferenceViewSet.as_view({'get': 'refbooks_elements_id'}),
        {'field': 'value'},
        name='values_elements'
    ),
    path(
        'refbooks/<id>/elements/',
        ElementReferenceViewSet.as_view({'get': 'refbooks_elements_name'}),
        name='all_elements'
    ),
    path(
        'refbooks/<id>/check_element',
        ElementReferenceViewSet.as_view({'get': 'check_element'}),
        name='all_elements'
    )
]
