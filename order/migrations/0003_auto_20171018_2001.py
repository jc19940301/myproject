# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_auto_20171018_1932'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderinfo',
            old_name='user',
            new_name='userinfo',
        ),
    ]
