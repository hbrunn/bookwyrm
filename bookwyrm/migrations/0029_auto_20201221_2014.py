# Generated by Django 3.0.7 on 2020-12-21 20:14

import bookwyrm.models.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bookwyrm', '0028_remove_book_author_text'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='last_sync_date',
        ),
        migrations.RemoveField(
            model_name='author',
            name='sync',
        ),
        migrations.RemoveField(
            model_name='book',
            name='last_sync_date',
        ),
        migrations.RemoveField(
            model_name='book',
            name='sync',
        ),
        migrations.RemoveField(
            model_name='book',
            name='sync_cover',
        ),
        migrations.AddField(
            model_name='author',
            name='goodreads_key',
            field=bookwyrm.models.fields.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='author',
            name='last_edited_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='author',
            name='librarything_key',
            field=bookwyrm.models.fields.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='last_edited_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='author',
            name='origin_id',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
