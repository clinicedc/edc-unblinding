# Generated by Django 3.2.13 on 2022-08-25 23:58

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "edc_unblinding",
            "0005_alter_historicalunblindingrequest_action_identifier_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="historicalunblindingrequest",
            name="action_identifier",
            field=models.CharField(blank=True, db_index=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name="historicalunblindingreview",
            name="action_identifier",
            field=models.CharField(blank=True, db_index=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name="unblindingrequest",
            name="action_identifier",
            field=models.CharField(blank=True, max_length=50, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name="unblindingreview",
            name="action_identifier",
            field=models.CharField(blank=True, max_length=50, null=True, unique=True),
        ),
    ]
