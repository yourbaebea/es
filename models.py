from django.db import models
from django.utils import timezone

#from django.contrib.auth.models import User #if we wanted to use the default users

# Create your models here.

#define values for prescription updates
class status(models.IntegerChoices):
    UNSTARTED = 0, 'unstarted'
    STARTED = 1, 'started'
    STEP_1 = 2, 'first'
    STEP_2= 3, 'second'
    STEP_3=4, 'third'
    FINNISHED=5, 'finnished'
    ERROR=-1, 'error'


class User(models.Model):
    name= models.TextField(max_length=50, blank=False)
    username= models.TextField(max_length=50, blank=False, unique=True)
    email= models.EmailField()
    password=models.CharField(max_length=15, blank=False)
    pharmacist= models.BooleanField(default=False)
    def __str__(self):
        return f'{self.username}'
   
class Medication(models.Model):
    name= models.TextField(max_length=50, blank=False, unique=True)
    alternatives = models.ManyToManyField('self', symmetrical=True, blank=True)
    price = models.DecimalField(default=10, blank=False, max_digits=10, decimal_places=2, verbose_name='Price (€)')
    def __str__(self):
        return f'{self.name}'

class Prescription(models.Model):
    patient = models.ForeignKey(User, on_delete=models.CASCADE)
    medications = models.ManyToManyField(Medication, through='PrescriptionMedication', through_fields=('prescription', 'medication'))
    filled= models.BooleanField()
    expiration_date= models.DateTimeField(default=timezone.now() + timezone.timedelta(days=30))
    status= models.IntegerField(default=status.UNSTARTED, choices=status.choices)
    def __str__(self):
        return f'Prescription for {self.patient}, status: {self.get_status_display()}'

class PrescriptionMedication(models.Model):
    prescription = models.ForeignKey(Prescription, on_delete=models.CASCADE)
    medication = models.ForeignKey(Medication, on_delete=models.CASCADE)
    dosage = models.IntegerField()
