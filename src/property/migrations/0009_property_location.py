# Generated by Django 2.1.7 on 2019-02-27 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0008_category_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='location',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
