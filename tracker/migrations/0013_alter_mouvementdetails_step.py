# Generated by Django 4.1.7 on 2023-02-18 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0012_alter_mouvementdetails_mouvements'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mouvementdetails',
            name='step',
            field=models.IntegerField(default=1),
        ),
    ]
