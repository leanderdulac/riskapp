from __future__ import unicode_literals

from django.db import models
from django.contrib import admin

# Create your models here.
    
class Risk_type(models.Model):
    description = models.CharField(max_length=15)

    def __unicode__(self):
        return self.description

class Control_Owners(models.Model):
    name = models.CharField(max_length=30,default='')

    def __unicode__(self):
        return unicode(self.name)

class control_status(models.Model):
    label = models.CharField(max_length=12,default='')

    def __unicode__(self):
        return unicode(self.label)

class Controls(models.Model):
    controlref = models.CharField(max_length=9)
    description = models.CharField(max_length=100)
    owner = models.ForeignKey(Control_Owners)
    type_of_control = models.CharField(max_length=60)
    status = models.ForeignKey(control_status)
    is_pci = models.CharField(max_length=1)
    is_cyber_essentials = models.CharField(max_length=1)
    is_iso27001 = models.CharField(max_length=1)
    is_gdpr = models.CharField(max_length=1)

    def __unicode__(self):
        return self.description

class Risk_Owners(models.Model):
    name = models.CharField(max_length=30)

    def __unicode__(self):
        return unicode(self.name)


class Likelihood_rating(models.Model):
    label = models.CharField(max_length=12)
    value = models.IntegerField(default='0')

    def __unicode__(self):
        return self.label

class Impact_rating(models.Model):
    label = models.CharField(max_length=12)
    value = models.IntegerField(default='0')

    def __unicode__(self):
        return self.label

class Res_Likelihood_rating(models.Model):
    label = models.CharField(max_length=12)
    value = models.IntegerField(default='0')

    def __unicode__(self):
        return self.label

class Risk(models.Model):
    riskref = models.CharField(max_length=9)
    description = models.CharField(max_length=100)
    owner = models.ForeignKey("Risk_Owners", on_delete=models.CASCADE)
    type_of_risk = models.ManyToManyField("Risk_type")
    created_date = models.DateTimeField('created on')
    last_updated_date = models.DateTimeField('last updated on')
    previous_updated_date = models.DateTimeField('previous update')
    AbsScore = models.IntegerField(null=True)
    ResScore = models.IntegerField(null=True)
    previous_score = models.IntegerField(default='0')
    ranking = models.IntegerField
    previous_ranking = models.IntegerField
    Absolute_Likelihood = models.ForeignKey("Likelihood_rating", on_delete=models.CASCADE)
    Absolute_Impact = models.ForeignKey("Impact_rating", on_delete=models.CASCADE)
    Rating_rationale = models.CharField(max_length=60)
    Residual_Likelihood = models.ForeignKey("Res_Likelihood_rating", on_delete=models.CASCADE)
    Associated_Controls = models.ManyToManyField("Controls")

    def __unicode__(self):
        return unicode(self.description)

    @property
    def AbsScore(self):
        return self.Absolute_Impact.value * self.Absolute_Likelihood.value

    @property
    def ResScore(self):
        return self.Absolute_Impact.value * self.Residual_Likelihood.value

class RiskAdmin(admin.ModelAdmin):     
    readonly_fields = ('AbsScore','ResScore',)
    ordering = ('riskref','Residual_Likelihood','Absolute_Likelihood','Absolute_Impact')
    list_display = ('riskref','description','AbsScore','Absolute_Impact','Absolute_Likelihood','ResScore','Residual_Likelihood','owner')

class ControlsAdmin(admin.ModelAdmin):     
    ordering = ('description','controlref','status')
    list_display = ('description','controlref','status','owner')
