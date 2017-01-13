# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0004_useranswer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='useranswer',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
