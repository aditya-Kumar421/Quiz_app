# Generated by Django 4.1.13 on 2024-01-10 11:39

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0007_remove_question_course_remove_userscore_quiz_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='question_uuid',
            field=models.UUIDField(default=uuid.uuid4, unique=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='question',
            field=models.CharField(max_length=100),
        ),
    ]
