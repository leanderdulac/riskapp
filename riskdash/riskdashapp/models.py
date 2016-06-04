from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Risk(models.Model):
    riskref = models.CharField(max_length=9)
    description = models.CharField(max_length=60)
    owner = models.ForeignKey("Risk_Owners", on_delete=models.CASCADE)
    created_date = models.DateTimeField('created on')
    last_updated_date = models.DateTimeField('last updated on')
    previous_updated_date = models.DateTimeField('previous update')
    Score = models.IntegerField
    previous_score = models.IntegerField
    ranking = models.IntegerField
    previous_ranking = models.IntegerField
    Absolute_Likelihood = models.ForeignKey("Likelihood_rating", on_delete=models.CASCADE)
    Absolute_Impact = models.ForeignKey("Impact_rating", on_delete=models.CASCADE)
    Rating_rationale = models.CharField(max_length=60)
    Residual_Likelihood = models.ForeignKey("Res_Likelihood_rating", on_delete=models.CASCADE)
    Associated_Controls = models.ManyToManyField("Controls")

    
class Risk_type(models.Model):
    description = models.CharField(max_length=15)

    def __unicode__(self):
        return self.description

class Controls(models.Model):
    controlref = models.CharField(max_length=9)
    description = models.CharField(max_length=60)
    owner = models.ForeignKey("Control_Owners", on_delete=models.CASCADE)
    type = models.CharField(max_length=60)
    status = models.ForeignKey("control_status", on_delete=models.CASCADE)
    is_pci = models.CharField(max_length=1)
    is_cyber_essentials = models.CharField(max_length=1)
    is_iso27001 = models.CharField(max_length=1)
    is_gdpr = models.CharField(max_length=1)

    def __unicode__(self):
        return self.status

class Risk_Owners(models.Model):
    name = models.CharField(max_length=30)

    def __unicode__(self):
        return self.name

class Control_Owners(models.Model):
    name = models.CharField(max_length=30)

    def __unicode__(self):
        return self.name

class Likelihood_rating(models.Model):
    label = models.CharField(max_length=12)
    value = models.IntegerField

    def __unicode__(self):
        return self.label

class Impact_rating(models.Model):
    label = models.CharField(max_length=12)
    value = models.IntegerField

    def __unicode__(self):
        return self.label

class Res_Likelihood_rating(models.Model):
    label = models.CharField(max_length=12)
    value = models.IntegerField

    def __unicode__(self):
        return self.label

class control_status(models.Model):
    label = models.CharField(max_length=12)

    def __unicode__(self):
        return self.label