# Generated by Django 3.0.7 on 2020-10-08 11:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('yaksh', '0025_release_0_26'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='course',
        ),
        migrations.AddField(
            model_name='forumbase',
            name='anonymous',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='post',
            name='target_ct',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='target_obj', to='contenttypes.ContentType'),
        ),
        migrations.AddField(
            model_name='post',
            name='target_id',
            field=models.PositiveIntegerField(blank=True, db_index=True, null=True),
        ),
    ]
