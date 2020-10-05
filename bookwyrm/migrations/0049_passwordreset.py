# Generated by Django 3.0.7 on 2020-10-02 19:43

import bookwyrm.models.site
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bookwyrm', '0048_generatednote'),
    ]

    operations = [
        migrations.CreateModel(
            name='PasswordReset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(default=bookwyrm.models.site.new_access_code, max_length=32)),
                ('expiry', models.DateTimeField(default=bookwyrm.models.site.get_passowrd_reset_expiry)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]