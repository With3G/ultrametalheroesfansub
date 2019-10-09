# Generated by Django 2.2.5 on 2019-10-02 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_auto_20191002_1016'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='serie',
            name='datos',
        ),
        migrations.AddField(
            model_name='serie',
            name='creador',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='serie',
            name='emision',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='serie',
            name='enlace',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='serie',
            name='episodios',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='serie',
            name='franquicia',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]
