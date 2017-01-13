# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0017_auto_20161214_1352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usertextanswer',
            name='my_answer',
            field=models.TextField(),
        ),
    ]
