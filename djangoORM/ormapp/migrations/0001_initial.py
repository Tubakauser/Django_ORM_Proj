# Generated by Django 4.1.2 on 2023-03-29 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(blank=True, max_length=50)),
            ],
        ),
    ]
