# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('signups', '0002_signup_for_you'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signup',
            name='for_you',
            field=models.BooleanField(default=True, verbose_name=b'Is this purchase for you? If so, check this '),
        ),
    ]
