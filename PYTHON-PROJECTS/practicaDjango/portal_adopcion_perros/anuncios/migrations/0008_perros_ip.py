# Generated by Django 3.0.6 on 2020-05-16 15:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('anuncios', '0007_perros_ultima_modificacion'),
    ]

    operations = [
        migrations.AddField(
            model_name='perros',
            name='ip',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]