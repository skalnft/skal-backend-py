# Generated by Django 4.2 on 2023-04-05 23:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('descricao', models.TextField()),
                ('data', models.DateTimeField()),
                ('localizacao', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Ingresso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nft_token_id', models.CharField(max_length=255)),
                ('valido', models.BooleanField(default=True)),
                ('evento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='evento.evento')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
