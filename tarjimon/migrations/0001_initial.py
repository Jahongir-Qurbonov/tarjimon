# Generated by Django 4.0.6 on 2022-08-05 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lugat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inglizcha', models.CharField(max_length=128)),
                ('uzbekcha', models.CharField(max_length=128)),
            ],
        ),
    ]
