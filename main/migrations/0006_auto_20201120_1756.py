# Generated by Django 3.1.2 on 2020-11-20 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20201120_1753'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='image',
        ),
        migrations.AddField(
            model_name='productoimage',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='products'),
        ),
    ]
