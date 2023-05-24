# Generated by Django 3.2.13 on 2022-08-26 00:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("edc_unblinding", "0006_auto_20220826_0258"),
    ]

    operations = [
        migrations.AlterField(
            model_name="historicalunblindingrequest",
            name="tracking_identifier",
            field=models.CharField(db_index=True, max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name="historicalunblindingreview",
            name="tracking_identifier",
            field=models.CharField(db_index=True, max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name="unblindingrequest",
            name="tracking_identifier",
            field=models.CharField(max_length=32, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name="unblindingreview",
            name="tracking_identifier",
            field=models.CharField(max_length=32, null=True, unique=True),
        ),
    ]
