# Generated by Django 4.2.7 on 2023-12-03 00:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "edc_unblinding",
            "0010_alter_historicalunblindingrequest_device_created_and_more",
        ),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="unblindingrequest",
            options={
                "default_manager_name": "objects",
                "default_permissions": (
                    "add",
                    "change",
                    "delete",
                    "view",
                    "export",
                    "import",
                ),
                "verbose_name": "Unblinding Request",
                "verbose_name_plural": "Unblinding Requests",
            },
        ),
        migrations.AlterModelOptions(
            name="unblindingreview",
            options={
                "default_manager_name": "objects",
                "default_permissions": (
                    "add",
                    "change",
                    "delete",
                    "view",
                    "export",
                    "import",
                ),
                "verbose_name": "Unblinding Review",
                "verbose_name_plural": "Unblinding Reviews",
            },
        ),
        migrations.AddField(
            model_name="historicalunblindingrequest",
            name="locale_created",
            field=models.CharField(
                blank=True,
                help_text="Auto-updated by Modeladmin",
                max_length=10,
                null=True,
                verbose_name="Locale created",
            ),
        ),
        migrations.AddField(
            model_name="historicalunblindingrequest",
            name="locale_modified",
            field=models.CharField(
                blank=True,
                help_text="Auto-updated by Modeladmin",
                max_length=10,
                null=True,
                verbose_name="Locale modified",
            ),
        ),
        migrations.AddField(
            model_name="historicalunblindingreview",
            name="locale_created",
            field=models.CharField(
                blank=True,
                help_text="Auto-updated by Modeladmin",
                max_length=10,
                null=True,
                verbose_name="Locale created",
            ),
        ),
        migrations.AddField(
            model_name="historicalunblindingreview",
            name="locale_modified",
            field=models.CharField(
                blank=True,
                help_text="Auto-updated by Modeladmin",
                max_length=10,
                null=True,
                verbose_name="Locale modified",
            ),
        ),
        migrations.AddField(
            model_name="unblindingrequest",
            name="locale_created",
            field=models.CharField(
                blank=True,
                help_text="Auto-updated by Modeladmin",
                max_length=10,
                null=True,
                verbose_name="Locale created",
            ),
        ),
        migrations.AddField(
            model_name="unblindingrequest",
            name="locale_modified",
            field=models.CharField(
                blank=True,
                help_text="Auto-updated by Modeladmin",
                max_length=10,
                null=True,
                verbose_name="Locale modified",
            ),
        ),
        migrations.AddField(
            model_name="unblindingreview",
            name="locale_created",
            field=models.CharField(
                blank=True,
                help_text="Auto-updated by Modeladmin",
                max_length=10,
                null=True,
                verbose_name="Locale created",
            ),
        ),
        migrations.AddField(
            model_name="unblindingreview",
            name="locale_modified",
            field=models.CharField(
                blank=True,
                help_text="Auto-updated by Modeladmin",
                max_length=10,
                null=True,
                verbose_name="Locale modified",
            ),
        ),
    ]
