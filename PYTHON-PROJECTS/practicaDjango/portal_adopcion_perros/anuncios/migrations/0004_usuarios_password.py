# Generated by Django 3.0.6 on 2020-05-08 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anuncios', '0003_auto_20200507_2022'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuarios',
            name='password',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
    ]
