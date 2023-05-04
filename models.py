from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#Using default User Model


    
class Drug(models.Model):
    name= models.TextField(max_length=100, blank=True, default='unnamed')
    def __str__(self):
        return f'Drug: {self.name}'

    
class Medication(models.Model):
    name= models.ForeignKey(Drug) #name of the medication
    dosage= models.IntegerField() #how much is prescribed
    def __str__(self):
        return f'Medication: {self.name}, Dosage: {self.dosage}'


class Prescription(models.Model):
    patient = models.ForeignKey(User, on_delete=models.CASCADE)
    doctor= models.ForeignKey(User)
    medication= models.ManyToManyField(Medication, blank=False)
    filled= models.BooleanField()
    expiration_date= models.DateTimeField()
    def __str__(self):
        return f'Prescription for {self.patient}: {self.name}, Dosage: {self.dosage}'

