# Generated by Django 5.0.4 on 2024-05-06 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blog_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='is_subscription',
            field=models.BooleanField(default=False, verbose_name='Подписка'),
        ),
    ]
