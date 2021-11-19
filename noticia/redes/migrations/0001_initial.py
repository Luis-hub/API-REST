# Generated by Django 3.2.9 on 2021-11-18 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Noticia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('autor', models.CharField(max_length=255)),
                ('titulo', models.CharField(max_length=255)),
                ('conteudo', models.CharField(max_length=255)),
                ('publicacao', models.CharField(max_length=255)),
                ('data', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
