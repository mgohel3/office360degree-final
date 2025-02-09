# Generated by Django 5.0.2 on 2024-02-09 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0015_option_label'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='option',
            name='label',
        ),
        migrations.RemoveField(
            model_name='option',
            name='value',
        ),
        migrations.AddField(
            model_name='option',
            name='nps_indicator',
            field=models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], default=0),
        ),
        migrations.AddField(
            model_name='option',
            name='text',
            field=models.CharField(default=None, max_length=128),
        ),
    ]
