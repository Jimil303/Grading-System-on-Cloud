# Generated by Django 3.1.7 on 2021-06-25 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grading', '0003_merge_20210622_1902'),
    ]

    operations = [
        migrations.CreateModel(
            name='Universities',
            fields=[
                ('name', models.CharField(db_column='name', max_length=75, primary_key=True, serialize=False)),
                ('username', models.CharField(db_column='username', max_length=25)),
                ('password', models.CharField(db_column='password', max_length=100)),
            ],
            options={
                'db_table': 'university',
            },
        ),
    ]