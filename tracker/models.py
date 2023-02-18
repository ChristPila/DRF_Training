from django.db import models


class Camions(models.Model):
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)


class Chauffeur(models.Model):
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)


status_choices1 = (
    ("En attente", "1"),
    ("En cours", "2"),
    ("Annulé", "3"),
    ("Cloturé", "4")
)

status_choices2 = (
    ("En cours", "1"),
    ("Terminé", "2")
)


class Mouvements(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=255, choices=status_choices1, default="1")
    remote_id = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    chauffeurs = models.ForeignKey('tracker.Chauffeur', on_delete=models.DO_NOTHING)
    camion = models.ForeignKey('tracker.Camions', blank=True, on_delete=models.DO_NOTHING)


class Steps(models.Model):
    checkpoint = models.CharField(max_length=255)
    step = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)


class MouvementDetails(models.Model):
    heure = models.TimeField(auto_now=True)
    status = models.CharField(max_length=255, choices=status_choices2, default="1")
    step = models.IntegerField(default=0)
    mouvements = models.ForeignKey('tracker.Mouvements', blank=True, on_delete=models.DO_NOTHING)



