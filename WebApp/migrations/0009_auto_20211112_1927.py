# Generated by Django 3.2.8 on 2021-11-12 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebApp', '0008_profile_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='historialCertamen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(auto_created=True)),
                ('id_usuario', models.IntegerField()),
                ('id_preguntas', models.CharField(max_length=50)),
                ('hora', models.DateTimeField(auto_now_add=True)),
                ('estado', models.BooleanField(default=False)),
            ],
        ),
        migrations.RemoveField(
            model_name='profile',
            name='email',
        ),
    ]
