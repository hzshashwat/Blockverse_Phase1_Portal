# Generated by Django 4.2 on 2023-05-12 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0007_schema_schemaasset'),
    ]

    operations = [
        migrations.AddField(
            model_name='schema',
            name='schema_year',
            field=models.IntegerField(default=1),
        ),
    ]