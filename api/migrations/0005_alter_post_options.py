# Generated by Django 4.1.7 on 2023-03-17 03:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_post_created_by'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('-created_at',)},
        ),
    ]
