# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0005_auto_20161107_1027'),
    ]

    operations = [
        migrations.RenameField(
            model_name='useranswer',
            old_name='answer',
            new_name='ans',
        ),
    ]
