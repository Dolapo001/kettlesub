# Generated by Django 5.0.2 on 2024-03-04 18:56

from django.db import migrations

from django.contrib.auth.hashers import make_password


def update_existing_passwords(apps, schema_editor):
    User = apps.get_model('Auth', 'User')

    users_to_update = User.objects.filter(password__isnull=True)
    for user in users_to_update:
        user.set_password('secure_default_password')
        user.save()


class Migration(migrations.Migration):

    dependencies = [
        ('Auth', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(update_existing_passwords),
    ]