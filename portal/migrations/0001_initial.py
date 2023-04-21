# Generated by Django 4.2 on 2023-04-21 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('team_name', models.CharField(max_length=150, null=True)),
                ('leader_name', models.CharField(max_length=150, null=True)),
                ('leader_email', models.CharField(max_length=150, null=True, unique=True)),
                ('leader_hosteler', models.CharField(max_length=150, null=True)),
                ('leader_year', models.CharField(max_length=150, null=True)),
                ('leader_branch', models.CharField(max_length=150, null=True)),
                ('leader_rollNo', models.CharField(max_length=150, null=True)),
                ('leader_phoneNo', models.CharField(max_length=150, null=True)),
                ('member_name', models.CharField(max_length=150, null=True)),
                ('member_phoneNo', models.CharField(max_length=150, null=True)),
                ('member_branch', models.CharField(max_length=150, null=True)),
                ('member_email', models.CharField(max_length=150, null=True)),
                ('member_rollNo', models.CharField(max_length=150, null=True)),
                ('member_hosteler', models.CharField(max_length=150, null=True)),
                ('member_year', models.CharField(max_length=150, null=True)),
                ('selected_schema', models.CharField(max_length=150, null=True)),
                ('final_submission_completed', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]