# Generated by Django 2.2 on 2019-04-30 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acora', '0011_auto_20190430_0746'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipo',
            name='puntaje',
            field=models.IntegerField(default=0),
        ),
    ]