# Generated by Django 5.0.7 on 2024-07-13 21:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0003_newcat'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='newcat',
            options={'verbose_name_plural': 'User categories'},
        ),
    ]
