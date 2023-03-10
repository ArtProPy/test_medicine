# Generated by Django 3.2.16 on 2023-01-17 17:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('medicine', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='elementreference',
            name='version_reference',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='elements_reference', to='medicine.versionreference', verbose_name='Идентификатор Версии справочника'),
        ),
        migrations.AlterField(
            model_name='reference',
            name='code',
            field=models.CharField(max_length=100, unique=True, verbose_name='Код'),
        ),
        migrations.AlterField(
            model_name='versionreference',
            name='reference',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='versions_reference', to='medicine.reference', verbose_name='Идентификатор справочника'),
        ),
        migrations.AlterUniqueTogether(
            name='elementreference',
            unique_together={('version_reference', 'code')},
        ),
        migrations.AlterUniqueTogether(
            name='versionreference',
            unique_together={('reference', 'date'), ('reference', 'version')},
        ),
    ]
