# Generated by Django 3.0.4 on 2020-05-14 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anuncios', '0005_anuncio_usuario'),
    ]

    operations = [
        migrations.AddField(
            model_name='anuncio',
            name='ip',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
    ]