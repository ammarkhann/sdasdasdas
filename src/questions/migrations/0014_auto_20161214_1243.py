# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0013_auto_20161214_1127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='freetextanswer',
            name='text',
            field=models.TextField(null=True, blank=True),
        ),
    ]
