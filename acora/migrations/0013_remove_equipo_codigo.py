# Generated by Django 2.2 on 2019-04-30 12:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('acora', '0012_auto_20190430_0748'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='equipo',
            name='codigo',
        ),
    ]