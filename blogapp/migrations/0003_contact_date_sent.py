# Generated by Django 4.2.1 on 2023-09-12 19:57

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0002_blog_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='date_sent',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
