# Generated by Django 4.1 on 2023-01-03 06:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recognition', '0003_attendance'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendance',
            name='userid',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='recognition.user'),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]