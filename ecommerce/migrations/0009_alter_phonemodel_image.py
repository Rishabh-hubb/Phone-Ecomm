# Generated by Django 4.1.1 on 2022-09-07 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ecommerce", "0008_alter_phonemodel_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="phonemodel",
            name="image",
            field=models.ImageField(default="no_image.png", upload_to="model-image"),
        ),
    ]
