from django.db import models


class Camions(models.Model):
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Chauffeur(models.Model):
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


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

    def __str__(self):
        return self.remote_id


class Steps(models.Model):
    checkpoint = models.CharField(max_length=255)
    step = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)


class MouvementDetails(models.Model):
    heure = models.TimeField(auto_now=True)
    date_op = models.DateTimeField(null=True)
    status = models.CharField(max_length=255, choices=status_choices2, default="1")
    checkpoint = models.CharField(max_length=255, null=True)
    step = models.IntegerField(default=0)
    mouvements = models.ForeignKey('tracker.Mouvements', blank=True, on_delete=models.DO_NOTHING)
    is_active = models.BooleanField(default=True)



