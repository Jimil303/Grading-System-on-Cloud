# Generated by Django 3.1.7 on 2021-06-20 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FacultyCredentials',
            fields=[
                ('username', models.CharField(db_column='username', max_length=50, primary_key=True, serialize=False)),
                ('password', models.CharField(db_column='password', max_length=100)),
                ('university', models.CharField(db_column='university', max_length=100)),
                ('auth', models.BooleanField(db_column='infoadded ', max_length=1)),
            ],
            options={
                'db_table': 'faculty_credentials',
            },
        ),
    ]
