# Generated by Django 2.2.5 on 2019-10-01 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20191001_2237'),
    ]

    operations = [
        migrations.AddField(
            model_name='entrada',
            name='imagen',
            field=models.ImageField(default=1, upload_to='static/img/archivo/'),
            preserve_default=False,
        ),
    ]
