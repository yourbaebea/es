from django.contrib import admin
from .models import User, Medication, Prescription, PrescriptionMedication

# Register your models here.

class PrescriptionMedicationInline(admin.TabularInline):
    model = PrescriptionMedication
    extra = 1

class MedicationForm(admin.ModelAdmin):
    inlines = [PrescriptionMedicationInline]

class MedicationAlternatives(admin.ModelAdmin):
    filter_horizontal = ('alternatives',)

    def save_model(self, request, obj, form, change):
        # save the Medication object
        obj.save()

        # update the alternatives for each of the object's alternatives
        for alt in obj.alternatives.all():
            alt.alternatives.add(obj)



admin.site.register(Prescription, MedicationForm)
admin.site.register(User)
admin.site.register(Medication, MedicationAlternatives)