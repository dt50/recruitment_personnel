# Generated by Django 4.0.4 on 2022-05-12 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='Address',
            field=models.CharField(default='Address', max_length=50),
        ),
        migrations.AddField(
            model_name='profile',
            name='City',
            field=models.CharField(default='City', max_length=50),
        ),
        migrations.AddField(
            model_name='profile',
            name='Country',
            field=models.CharField(default='Country', max_length=50),
        ),
        migrations.AddField(
            model_name='profile',
            name='PasportCode',
            field=models.CharField(default='Pasport code', max_length=15),
        ),
        migrations.AddField(
            model_name='profile',
            name='PasportDate',
            field=models.CharField(default='Pasport date', max_length=15),
        ),
        migrations.AddField(
            model_name='profile',
            name='PasportNum',
            field=models.CharField(default='Pasport num', max_length=15),
        ),
        migrations.AddField(
            model_name='profile',
            name='PasportOtd',
            field=models.CharField(default='Pasport otd', max_length=50),
        ),
        migrations.AddField(
            model_name='profile',
            name='Region',
            field=models.CharField(default='Region', max_length=50),
        ),
        migrations.AddField(
            model_name='profile',
            name='inn_fiz',
            field=models.CharField(default='inn', max_length=15),
        ),
        migrations.AddField(
            model_name='profile',
            name='login',
            field=models.CharField(default='login', max_length=30),
        ),
        migrations.AddField(
            model_name='profile',
            name='oms',
            field=models.CharField(default='oms', max_length=15),
        ),
    ]