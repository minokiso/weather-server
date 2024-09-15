# Generated by Django 4.2.11 on 2024-09-08 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0002_alter_weather3h_airtemperature_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DateTime', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'log',
                'ordering': ['DateTime'],
            },
        ),
        migrations.AlterField(
            model_name='weather3h',
            name='DateTime',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]