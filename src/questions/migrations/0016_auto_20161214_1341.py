# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('questions', '0015_auto_20161214_1332'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserTextAnswer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('my_points', models.IntegerField(default=-1)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('my_answer', models.ForeignKey(to='questions.FreeTextAnswer')),
                ('question', models.ForeignKey(to='questions.Question')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='answer',
            name='text',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
