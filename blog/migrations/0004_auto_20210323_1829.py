# Generated by Django 3.1.7 on 2021-03-23 11:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20210323_1726'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'ordering': ['post_date']},
        ),
    ]
