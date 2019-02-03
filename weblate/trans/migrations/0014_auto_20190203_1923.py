# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-02-03 18:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trans', '0013_component_addon_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='whiteboardmessage',
            name='expiry',
            field=models.DateField(blank=True, db_index=True, help_text='The message will be not shown after this date. Use for announcements such as deadline for next release.', null=True, verbose_name='Expiry date'),
        ),
        migrations.AlterField(
            model_name='whiteboardmessage',
            name='category',
            field=models.CharField(choices=[(b'info', 'Info (light blue)'), (b'warning', 'Warning (yellow)'), (b'danger', 'Danger (red)'), (b'success', 'Success (green)')], default=b'info', help_text='Category defines color used for the message.', max_length=25, verbose_name='Category'),
        ),
    ]
