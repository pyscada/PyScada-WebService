# Generated by Django 2.2.8 on 2020-09-02 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webservice', '0004_auto_20200902_1027'),
    ]

    operations = [
        migrations.AddField(
            model_name='webservicevariable',
            name='path',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
    ]