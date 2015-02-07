# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oldgold', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GoldPrice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rate', models.DecimalField(max_digits=25, decimal_places=10)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RenameField(
            model_name='item',
            old_name='valid_until',
            new_name='valid_for',
        ),
    ]
