# Generated by Django 4.0.4 on 2022-06-17 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Juegos', '0004_usuarios'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuarios2',
            fields=[
                ('IdUsuarios', models.AutoField(primary_key=True, serialize=False, verbose_name='ID autoincrementable de los usuarios')),
                ('nombreUsuario', models.CharField(max_length=20, verbose_name='Nombre de los usuarios')),
            ],
        ),
    ]
