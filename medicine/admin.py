from django.contrib import admin

from medicine.models import Reference, VersionReference, ElementReference


class VersionReferenceInLine(admin.StackedInline):
    model = VersionReference

    def get_extra(self, request, obj=None, **kwargs):
        return 0


class ElementReferenceInLine(admin.StackedInline):
    model = ElementReference

    def get_extra(self, request, obj=None, **kwargs):
        return 0


@admin.register(Reference)
class ReferenceAdmin(admin.ModelAdmin):
    list_display = ('id', 'code', 'name', 'version', 'version_data')
    inlines = (VersionReferenceInLine,)
    ordering = ('code',)

    @admin.display(description='Текущая версия')
    def version(self, obj):
        return obj.versions_reference.last().version if obj.versions_reference.all() else 'Справочник не имеет версий'

    @admin.display(description='Дата начала действия версии')
    def version_data(self, obj):
        return obj.versions_reference.last().date if obj.versions_reference.all() else 'Справочник не имеет версий'


@admin.register(VersionReference)
class VersionReferenceAdmin(admin.ModelAdmin):
    list_display = ('reference_code', 'reference', 'version', 'date')
    inlines = (ElementReferenceInLine,)
    ordering = ('reference', 'version')

    @admin.display(description='Код справочника')
    def reference_code(self, obj):
        return obj.reference.code


@admin.register(ElementReference)
class ElementReferenceAdmin(admin.ModelAdmin):
    list_display = ('version_reference', 'code', 'value')
    ordering = ('version_reference',)
