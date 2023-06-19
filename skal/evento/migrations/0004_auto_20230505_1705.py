# Generated by Django 3.2.18 on 2023-05-05 17:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_currentuser.db.models.fields
import django_currentuser.middleware


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('evento', '0003_ingresso_preco'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingresso',
            name='usuario',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Venda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('preco_total', models.FloatField()),
                ('data_venda', models.DateTimeField()),
                ('forma_pagamento', models.CharField(choices=[], max_length=255)),
                ('ingresso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='evento.ingresso')),
                ('usuario', django_currentuser.db.models.fields.CurrentUserField(default=django_currentuser.middleware.get_current_authenticated_user, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]