# Generated by Django 4.0.2 on 2024-05-15 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0004_alter_cinemahall_rows_alter_cinemahall_seats_in_row'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='description',
            field=models.TextField(default=None),
        ),
    ]
