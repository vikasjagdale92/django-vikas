# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-09-13 11:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentmaster',
            name='question',
        ),
        migrations.AlterField(
            model_name='choice',
            name='choice_text',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='choice',
            name='votes',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='question',
            name='answer',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='question',
            name='option_A',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='question',
            name='option_B',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='question',
            name='option_C',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='question',
            name='option_D',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_text',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='studentmaster',
            name='address',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='studentmaster',
            name='blood_group',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='studentmaster',
            name='city',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='studentmaster',
            name='country',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='studentmaster',
            name='first_name',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='studentmaster',
            name='gender',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='studentmaster',
            name='last_name',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='studentmaster',
            name='mobile_number',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='studentmaster',
            name='pincode',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='studentmaster',
            name='school_name',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='studentmaster',
            name='standard',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='studentmaster',
            name='state',
            field=models.CharField(default='', max_length=200),
        ),
    ]