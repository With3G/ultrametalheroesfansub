# Generated by Django 2.2.5 on 2019-10-02 10:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0013_auto_20191002_0958'),
    ]

    operations = [
        migrations.CreateModel(
            name='Catalogo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('poster', models.ImageField(upload_to='series')),
                ('capturaUno', models.ImageField(upload_to='archivo')),
                ('capturaDos', models.ImageField(upload_to='archivo')),
                ('capturaTres', models.ImageField(upload_to='archivo')),
                ('capturaCuatro', models.ImageField(upload_to='archivo')),
                ('datos', models.TextField()),
                ('sipnosis', models.TextField()),
                ('activa', models.BooleanField(default=True)),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
