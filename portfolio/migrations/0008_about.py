# Generated by Django 2.1.7 on 2019-02-23 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0007_auto_20190223_1842'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about', models.CharField(max_length=500, verbose_name='About')),
                ('resume', models.FileField(upload_to='resume')),
                ('portfolioURL', models.URLField(null=True)),
            ],
        ),
    ]
