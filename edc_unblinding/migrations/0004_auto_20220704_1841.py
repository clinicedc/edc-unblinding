# Generated by Django 3.2.13 on 2022-07-04 15:41

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("edc_unblinding", "0003_auto_20210911_2036"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="historicalunblindingrequest",
            options={
                "get_latest_by": ("history_date", "history_id"),
                "ordering": ("-history_date", "-history_id"),
                "verbose_name": "historical Unblinding Request",
                "verbose_name_plural": "historical Unblinding Requests",
            },
        ),
        migrations.AlterModelOptions(
            name="historicalunblindingreview",
            options={
                "get_latest_by": ("history_date", "history_id"),
                "ordering": ("-history_date", "-history_id"),
                "verbose_name": "historical Unblinding Review",
                "verbose_name_plural": "historical Unblinding Reviews",
            },
        ),
        migrations.AlterField(
            model_name="historicalunblindingrequest",
            name="history_date",
            field=models.DateTimeField(db_index=True),
        ),
        migrations.AlterField(
            model_name="historicalunblindingreview",
            name="history_date",
            field=models.DateTimeField(db_index=True),
        ),
    ]
