# Generated by Django 4.1.13 on 2024-02-05 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0011_remove_userscore_question'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='option_four',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='option_one',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='option_three',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='option_two',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
