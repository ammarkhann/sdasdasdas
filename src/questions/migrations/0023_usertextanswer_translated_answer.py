# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0022_question_question_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='usertextanswer',
            name='translated_answer',
            field=models.TextField(null=True, blank=True),
        ),
    ]
