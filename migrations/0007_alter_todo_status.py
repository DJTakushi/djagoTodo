# Generated by Django 4.0.6 on 2022-08-11 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoTask', '0006_alter_todo_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='status',
            field=models.CharField(blank=True, default='open', max_length=100, null=True),
        ),
    ]