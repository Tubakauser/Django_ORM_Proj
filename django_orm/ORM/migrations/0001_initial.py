# Generated by Django 4.1.4 on 2023-07-21 09:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='dept',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dept_id', models.IntegerField()),
                ('dept_name', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='emp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_id', models.IntegerField()),
                ('emp_name', models.CharField(max_length=150)),
                ('emp_salary', models.IntegerField()),
                ('dept_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ORM.dept')),
            ],
        ),
    ]
