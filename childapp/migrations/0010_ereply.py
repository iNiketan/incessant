# Generated by Django 3.1.4 on 2021-01-05 12:35

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('childapp', '0009_auto_20210103_1243'),
    ]

    operations = [
        migrations.CreateModel(
            name='EReply',
            fields=[
                ('r_sno', models.AutoField(primary_key=True, serialize=False)),
                ('reply', models.TextField()),
                ('timestamp', models.DateTimeField(default=datetime.datetime.now)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='childapp.ques')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
