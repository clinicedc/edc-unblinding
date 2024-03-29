# Generated by Django 4.2.1 on 2023-07-07 19:32

import edc_identifier.managers
import edc_sites.models
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("edc_unblinding", "0008_auto_20220826_0406"),
    ]

    operations = [
        migrations.AlterModelManagers(
            name="unblindingrequest",
            managers=[
                ("objects", edc_identifier.managers.SubjectIdentifierManager()),
                ("on_site", edc_sites.models.CurrentSiteManager()),
            ],
        ),
        migrations.AlterModelManagers(
            name="unblindingreview",
            managers=[
                ("objects", edc_identifier.managers.SubjectIdentifierManager()),
                ("on_site", edc_sites.models.CurrentSiteManager()),
            ],
        ),
    ]
