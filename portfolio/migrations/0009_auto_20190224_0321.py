# Generated by Django 2.1.7 on 2019-02-23 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0008_about'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='resume',
            field=models.FileField(upload_to='uploads/%Y/%m/%d/'),
        ),
    ]