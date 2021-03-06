# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-09-13 11:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_text', models.CharField(default='R U OK!', max_length=200)),
                ('votes', models.CharField(default='0', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(default="What's up?", max_length=200)),
                ('option_A', models.CharField(default='A', max_length=200)),
                ('option_B', models.CharField(default='B', max_length=200)),
                ('option_C', models.CharField(default='C', max_length=200)),
                ('option_D', models.CharField(default='D', max_length=200)),
                ('answer', models.CharField(default='A', max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
        migrations.CreateModel(
            name='StudentMaster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default='John', max_length=200)),
                ('last_name', models.CharField(default='LEE', max_length=200)),
                ('DOB', models.DateField(verbose_name='date of birth')),
                ('gender', models.CharField(default='Female', max_length=200)),
                ('blood_group', models.CharField(default='AB+', max_length=200)),
                ('standard', models.CharField(default='10th', max_length=200)),
                ('mobile_number', models.CharField(default='8888433075', max_length=200)),
                ('school_name', models.CharField(default='A', max_length=200)),
                ('address', models.CharField(default='address', max_length=200)),
                ('country', models.CharField(default='India', max_length=200)),
                ('state', models.CharField(default='Maharashtra', max_length=200)),
                ('city', models.CharField(default='Pune', max_length=200)),
                ('pincode', models.CharField(default='410506', max_length=200)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Question')),
            ],
        ),
        migrations.AddField(
            model_name='choice',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Question'),
        ),
    ]
