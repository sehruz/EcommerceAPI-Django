# Generated by Django 4.1.5 on 2023-01-13 11:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("DjangoAPIapp", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="book", options={"ordering": ["-date_created"]},
        ),
        migrations.AlterModelOptions(
            name="product", options={"ordering": ["-date_created"]},
        ),
    ]
