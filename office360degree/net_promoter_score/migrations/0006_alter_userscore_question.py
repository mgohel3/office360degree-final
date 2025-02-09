# Generated by Django 5.0.2 on 2024-02-24 07:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('net_promoter_score', '0005_remove_question_category_and_more'),
        ('survey', '0025_surveyquestion_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userscore',
            name='question',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_scores', to='survey.surveyquestion'),
        ),
    ]
