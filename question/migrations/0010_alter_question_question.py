# Generated by Django 4.1.13 on 2024-01-10 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0009_remove_question_question_uuid_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='question',
            field=models.CharField(max_length=255),
        ),
    ]
