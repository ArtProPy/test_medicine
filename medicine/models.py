from django.db import models


class Reference(models.Model):
    name = models.CharField('Наименование ', max_length=300)
    code = models.CharField('Код', max_length=100, unique=True)
    description = models.TextField('Описание ', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'medicine'
        verbose_name = 'Справочник'
        verbose_name_plural = 'Справочники'


class VersionReference(models.Model):
    reference = models.ForeignKey(
        Reference,
        on_delete=models.CASCADE,
        related_name='versions_reference',
        verbose_name='Идентификатор справочника'
    )
    version = models.CharField('Версия', max_length=50)
    date = models.DateField('Дата')

    def __str__(self):
        return self.version

    class Meta:
        app_label = 'medicine'
        unique_together = (('reference', 'version'), ('reference', 'date'))
        verbose_name = 'Версия справочника'
        verbose_name_plural = 'Версии справочника'


class ElementReference(models.Model):
    version_reference = models.ForeignKey(
        VersionReference,
        on_delete=models.CASCADE,
        related_name='elements_reference',
        verbose_name='Идентификатор Версии справочника'
    )
    code = models.CharField('Код элемента', max_length=100)
    value = models.CharField('Значение элемента', max_length=100)

    def __str__(self):
        return self.value

    class Meta:
        app_label = 'medicine'
        unique_together = ('version_reference', 'code')
        verbose_name = 'Элемент справочника'
        verbose_name_plural = 'Элементы справочника'
