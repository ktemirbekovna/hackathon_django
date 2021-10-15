from django.db import models


class hospital(models.Model):
    pass

class Hosp(models.Model):
    del_info = models.ForeignKey(hospital, on_delete=models.CASCADE)
    hosp_name = models.CharField(max_length=100)
    hosp_number = models.CharField(max_length=100)
    hosp_maindoc = models.CharField(max_length=155)
    hosp_docs = models.IntegerField()
    hosp_nurses = models.IntegerField()
    hosp_patients = models.IntegerField()


class Maindoctor(models.Model):
    del_info = models.ForeignKey(hospital, on_delete=models.CASCADE)
    doctor_name = models.CharField(max_length=100)
    doctor_work = models.CharField(max_length=100)
    doctor_experience = models.CharField(max_length=100)
    doctor_number = models.CharField(max_length=100)
    doctor_sawbones = models.IntegerField()
    doctor_therapist = models.IntegerField()
    doctor_nurses = models.IntegerField()

class Sawbones(models.Model):
    del_info = models.ForeignKey(hospital, on_delete=models.CASCADE)
    doctor_name = models.CharField(max_length=100)
    doctor_work = models.CharField(max_length=100)
    doctor_experience = models.CharField(max_length=100)
    doctor_number = models.CharField(max_length=100)
    doctor_nurses = models.IntegerField()
    doctor_patients = models.CharField(max_length=200)


class Therapist(models.Model):
    del_info = models.ForeignKey(hospital, on_delete=models.CASCADE)
    doctor_name = models.CharField(max_length=100)
    doctor_work = models.CharField(max_length=100)
    doctor_experience = models.CharField(max_length=100)
    doctor_number = models.CharField(max_length=100)
    doctor_nurse = models.CharField(max_length=100)
    doctor_pasients = models.CharField(max_length=200)


class Nurses(models.Model):
    del_info = models.ForeignKey(hospital, on_delete=models.CASCADE)
    doctor_name = models.CharField(max_length=100)
    doctor_work = models.CharField(max_length=100)
    doctor_experience = models.CharField(max_length=100)
    doctor_number = models.CharField(max_length=100)
    doctor_patients = models.CharField(max_length=200)

class Patients(models.Model):
    del_info = models.ForeignKey(hospital, on_delete=models.CASCADE)
    patient_name = models.CharField(max_length=100)
    patient_number = models.CharField(max_length=100)
    patient_doc = models.CharField(max_length=100)
    patient_diagnostic = models.CharField(max_length=255)

