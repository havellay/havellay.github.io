# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oldgold', '0002_auto_20150203_1706'),
    ]

    operations = [
        migrations.CreateModel(
            name='DetailImg',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('detail_img', models.ImageField(upload_to=b'images/products/')),
                ('item', models.ForeignKey(to='oldgold.Item')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RenameField(
            model_name='item',
            old_name='image',
            new_name='cover_img',
        ),
    ]
