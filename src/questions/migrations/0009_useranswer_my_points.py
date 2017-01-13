# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0008_useranswer'),
    ]

    operations = [
        migrations.AddField(
            model_name='useranswer',
            name='my_points',
            field=models.IntegerField(default=-1),
        ),
    ]
