# Generated by Django 3.0.4 on 2020-03-09 11:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_comment'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
