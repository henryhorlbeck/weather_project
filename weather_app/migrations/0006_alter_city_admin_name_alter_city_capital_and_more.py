# Generated by Django 4.1.7 on 2023-03-02 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather_app', '0005_alter_city_lat_alter_city_lng'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='admin_name',
            field=models.CharField(max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='city',
            name='capital',
            field=models.CharField(max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='city',
            name='city_id',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='city',
            name='country',
            field=models.CharField(max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='city',
            name='iso2',
            field=models.CharField(max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='city',
            name='iso3',
            field=models.CharField(max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='city',
            name='lat',
            field=models.DecimalField(decimal_places=3, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='city',
            name='lng',
            field=models.DecimalField(decimal_places=3, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='city',
            name='name',
            field=models.CharField(max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='city',
            name='name_asci',
            field=models.CharField(max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='city',
            name='population',
            field=models.IntegerField(null=True),
        ),
    ]
