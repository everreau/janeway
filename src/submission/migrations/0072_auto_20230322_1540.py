# Generated by Django 3.2.16 on 2023-03-22 15:40

from django.db import migrations
import django_bleach.models


class Migration(migrations.Migration):

    dependencies = [
        ('submission', '0071_merge_0070_auto_20230120_1546_0070_auto_20230208_1233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='abstract',
            field=django_bleach.models.BleachField(blank=True, help_text='Copying and pasting from word processors is supported.', null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='abstract_cy',
            field=django_bleach.models.BleachField(blank=True, help_text='Copying and pasting from word processors is supported.', null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='abstract_de',
            field=django_bleach.models.BleachField(blank=True, help_text='Copying and pasting from word processors is supported.', null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='abstract_en',
            field=django_bleach.models.BleachField(blank=True, help_text='Copying and pasting from word processors is supported.', null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='abstract_en_us',
            field=django_bleach.models.BleachField(blank=True, help_text='Copying and pasting from word processors is supported.', null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='abstract_fr',
            field=django_bleach.models.BleachField(blank=True, help_text='Copying and pasting from word processors is supported.', null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='abstract_nl',
            field=django_bleach.models.BleachField(blank=True, help_text='Copying and pasting from word processors is supported.', null=True),
        ),
    ]