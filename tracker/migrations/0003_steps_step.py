# Generated by Django 4.1.7 on 2023-02-15 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0002_alter_mouvementdetails_mouvements_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='steps',
            name='step',
            field=models.IntegerField(default=0),
        ),
    ]
