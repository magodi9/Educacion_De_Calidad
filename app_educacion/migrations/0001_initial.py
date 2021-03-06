# Generated by Django 3.2.7 on 2021-12-11 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Proyecto',
            fields=[
                ('proyecto_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('titulo_proyecto', models.CharField(max_length=50, verbose_name='Titulo Proyecto')),
                ('resumen', models.CharField(max_length=255, verbose_name='Resumen')),
                ('objetivos', models.CharField(max_length=255, verbose_name='Objetivos')),
                ('conclusiones', models.CharField(max_length=255, verbose_name='Conclusiones')),
                ('metodologia', models.CharField(max_length=255, verbose_name='Metodologia')),
                ('presupuesto', models.IntegerField(verbose_name='Presupuesto')),
                ('fecha_inicio', models.DateField(max_length=50, verbose_name='Fecha de Inicio')),
                ('fecha_cierre', models.DateField(max_length=50, verbose_name='Fecha de Cierre')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('cedula', models.CharField(max_length=20, unique=True, verbose_name='Cedula')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre')),
                ('correo_electronico', models.CharField(max_length=100, verbose_name='Correo Electronico')),
                ('direccion', models.CharField(max_length=250, verbose_name='Direccion')),
                ('password', models.CharField(max_length=20, verbose_name='Password')),
                ('departamento', models.CharField(max_length=50, verbose_name='Deparatamento')),
                ('municipio_de_residencia', models.CharField(max_length=50, verbose_name='Municipio de Residencia')),
                ('perfil', models.CharField(max_length=20, verbose_name='Perfil')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
