# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class User(models.Model):
    name = models.CharField(max_length=20)
    balance = models.DecimalField(max_digits=6, decimal_places=2)

    class Meta:
        managed = True
        db_table = 'user'

    def __str__(self):
        return self.name, self.balance


class SpoPulse(models.Model):
    spo2 = models.IntegerField()
    bpm = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'bpm_spo2Data'

    def __str__(self):
        return self.spo2, self.bpm


class bloodpressure_signal(models.Model):
    diastolic = models.IntegerField()
    systolic = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'bloodpressure_signal'

    def __str__(self):
        return self.diastolic, self.systolic


class emg_signal(models.Model):
    emg_voltage = models.DecimalField(max_digits=5, decimal_places=4)

    class Meta:
        managed = True
        db_table = 'emg_signal'

    def __str__(self):
        return self.emg_voltage