# Generated by Django 3.1.4 on 2021-01-14 06:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('childapp', '0010_ereply'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ereply',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='childapp.contactus'),
        ),
        migrations.AlterField(
            model_name='ques',
            name='img',
            field=models.ImageField(blank=True, default='default.png', upload_to=''),
        ),
    ]
