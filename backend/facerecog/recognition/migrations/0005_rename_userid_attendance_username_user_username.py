# Generated by Django 4.1 on 2023-01-03 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recognition', '0004_attendance_userid_alter_attendance_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='attendance',
            old_name='userid',
            new_name='username',
        ),
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(default='user', max_length=20),
        ),
    ]
