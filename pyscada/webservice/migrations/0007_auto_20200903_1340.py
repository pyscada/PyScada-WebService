# Generated by Django 2.2.8 on 2020-09-03 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webservice', '0006_auto_20200902_1328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='webservicevariable',
            name='path',
            field=models.CharField(blank=True, help_text='For XML look at https://docs.python.org/3/library/xml.etree.elementtree.html#xpath-support', max_length=254, null=True),
        ),
    ]