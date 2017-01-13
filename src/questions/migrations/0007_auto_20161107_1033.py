# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0006_auto_20161107_1031'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='useranswer',
            name='ans',
        ),
        migrations.RemoveField(
            model_name='useranswer',
            name='question',
        ),
        migrations.RemoveField(
            model_name='useranswer',
            name='user',
        ),
        migrations.DeleteModel(
            name='UserAnswer',
        ),
    ]
