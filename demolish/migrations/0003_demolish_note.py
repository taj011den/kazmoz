# Generated by Django 3.1.4 on 2024-04-23 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demolish', '0002_auto_20240423_1045'),
    ]

    operations = [
        migrations.AddField(
            model_name='demolish',
            name='note',
            field=models.CharField(default=1, max_length=50, verbose_name='Enter Your Notic'),
            preserve_default=False,
        ),
    ]