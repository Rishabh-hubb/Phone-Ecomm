# Generated by Django 4.1.1 on 2022-09-07 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ecommerce", "0003_code"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="phone",
            field=models.CharField(max_length=13),
        ),
    ]
