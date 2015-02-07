# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(upload_to=b'images/products/')),
                ('description', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name=b'date published')),
                ('valid_until', models.IntegerField(verbose_name=b'valid until')),
                ('weight', models.DecimalField(max_digits=19, decimal_places=10)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
