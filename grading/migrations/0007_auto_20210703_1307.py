# Generated by Django 3.1.7 on 2021-07-03 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grading', '0006_auto_20210703_1229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facultycredentials',
            name='username',
            field=models.CharField(db_column='username', max_length=25, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='studentcredentials',
            name='username',
            field=models.CharField(db_column='username', max_length=25, primary_key=True, serialize=False),
        ),
    ]