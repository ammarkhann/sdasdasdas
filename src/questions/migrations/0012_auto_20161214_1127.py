# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0011_auto_20161214_1125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='freetextanswer',
            name='text',
            field=models.TextField(null=True),
        ),
    ]
