# Generated by Django 3.2.8 on 2022-04-15 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_room_desc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='desc',
            field=models.TextField(blank=True, null=True),
        ),
    ]
