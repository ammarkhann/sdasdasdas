# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0021_auto_20161215_1035'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='question_type',
            field=models.CharField(default=1, max_length=250, choices=[(b'multiple_choice', b'multiple_choice'), (b'text_input', b'text_input')]),
            preserve_default=False,
        ),
    ]
