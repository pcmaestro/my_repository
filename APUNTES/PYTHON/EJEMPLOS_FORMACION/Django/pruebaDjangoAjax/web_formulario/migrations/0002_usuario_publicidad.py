# Generated by Django 3.0.6 on 2020-06-03 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_formulario', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='publicidad',
            field=models.BooleanField(default=0),
            preserve_default=False,
        ),
    ]