import factory

from medicine import models as medicine_models


class ReferenceFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = medicine_models.Reference
        django_get_or_create = ('id',)

    id = factory.Faker('pyint', min_value=0)
    name = factory.Faker('name')
    code = factory.Faker('name')
    description = factory.Faker('text')


class VersionReferenceFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = medicine_models.VersionReference
        django_get_or_create = ('id',)

    id = factory.Faker('pyint', min_value=0)
    reference = factory.SubFactory(ReferenceFactory)
    version = factory.Faker('name')
    date = factory.Faker('date')


class ElementReferenceFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = medicine_models.ElementReference

    id = factory.Faker('pyint', min_value=0)
    version_reference = factory.SubFactory(VersionReferenceFactory)
    code = factory.Faker('name')
    value = factory.Faker('name')
