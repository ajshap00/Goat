# Generated by Django 5.1.2 on 2024-10-31 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vote',
            name='voter_ip',
            field=models.GenericIPAddressField(),
        ),
    ]
