# Generated by Django 4.1.7 on 2023-02-18 00:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0011_alter_mouvements_camion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mouvementdetails',
            name='mouvements',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, to='tracker.mouvements'),
        ),
    ]