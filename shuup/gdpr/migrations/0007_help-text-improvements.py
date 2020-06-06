# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2020-01-29 09:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shuup_gdpr', '0006_category_default_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gdprsettingstranslation',
            name='auth_consent_text',
            field=models.TextField(blank=True, help_text='Shown in login page between the form and the button. Optional, but should be considered when the consent on login is disabled.', verbose_name='login consent text'),
        ),
    ]