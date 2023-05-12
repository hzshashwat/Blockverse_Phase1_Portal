# Generated by Django 4.2 on 2023-05-12 05:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0006_alter_userprofile_leader_email_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Schema',
            fields=[
                ('schema_id', models.IntegerField(primary_key=True, serialize=False)),
                ('schema_name', models.CharField(max_length=150, null=True)),
                ('image_url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='SchemaAsset',
            fields=[
                ('schema_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='portal.schema')),
                ('asset_name', models.CharField(max_length=200, null=True)),
                ('asset_url', models.URLField()),
            ],
        ),
    ]
