# Generated by Django 2.1.7 on 2019-02-27 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0007_reserve'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(null=True, upload_to='category/'),
        ),
    ]