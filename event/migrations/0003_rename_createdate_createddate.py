# Generated by Django 5.1.1 on 2024-12-21 13:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0002_createdate_date'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CreateDate',
            new_name='CreatedDate',
        ),
    ]
