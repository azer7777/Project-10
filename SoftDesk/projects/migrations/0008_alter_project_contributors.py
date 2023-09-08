# Generated by Django 4.2.4 on 2023-09-08 03:37

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projects', '0007_alter_comment_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='contributors',
            field=models.ManyToManyField(blank=True, null=True, related_name='contributed_projects', to=settings.AUTH_USER_MODEL),
        ),
    ]
