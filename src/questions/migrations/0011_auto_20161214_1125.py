# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0010_freetextanswer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='freetextanswer',
            name='text',
            field=models.CharField(max_length=500),
        ),
    ]
