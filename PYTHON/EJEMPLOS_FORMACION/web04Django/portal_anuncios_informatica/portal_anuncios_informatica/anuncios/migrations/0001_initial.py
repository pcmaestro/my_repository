# Generated by Django 3.0.4 on 2020-05-05 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Anuncio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('precio', models.FloatField(default=0)),
                ('email', models.CharField(max_length=150)),
            ],
        ),
    ]