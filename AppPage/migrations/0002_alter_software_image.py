# Generated by Django 4.1.7 on 2023-02-23 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppPage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='software',
            name='image',
            field=models.URLField(),
        ),
    ]
