# Generated by Django 3.0.1 on 2019-12-30 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='stack',
            field=models.CharField(max_length=200, null=True),
        ),
    ]