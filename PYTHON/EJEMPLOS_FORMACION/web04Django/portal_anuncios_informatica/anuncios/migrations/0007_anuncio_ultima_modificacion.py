# Generated by Django 3.0.4 on 2020-05-14 08:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('anuncios', '0006_anuncio_ip'),
    ]

    operations = [
        migrations.AddField(
            model_name='anuncio',
            name='ultima_modificacion',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='ultima modificacion'),
            preserve_default=False,
        ),
    ]
