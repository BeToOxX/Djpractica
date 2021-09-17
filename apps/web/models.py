from django.db import models

# Create your models here.
class petshop (models.Model):
    pk_petshop = models.AutoField(primary_key=True, null=False, blank=False)
    name = models.CharField(max_length=20, null=False, blank=False)
    direction = models.TextField(null=False, blank=False)
    phone = models.IntegerField(null=False, blank=False)
    owner = models.CharField(max_length=20, null=False, blank=False)

    class Meta:
        verbose_name = 'petshop'
        verbose_name_plural = 'petshops'
        ordering = ['name']

    def __str__(self):
        return "{0}".format(self.name)

class pet (models.Model):
    pk_pet = models.AutoField(primary_key=True, null=False, blank=False)
    name = models.CharField(max_length=15, null=False, blank=False)
    race = models.CharField(max_length=25, null=False, blank=False)
    gender = models.CharField(max_length=10, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    age = models.CharField(max_length=10, null=False, blank=False)
    image = models.URLField(max_length=8000, null=False, blank=False, default='https://st.depositphotos.com/1967477/1959/v/600/depositphotos_19591553-stock-illustration-cute-cat-cartoon.jpg')

    class Meta:
        verbose_name = 'pet'
        verbose_name_plural = 'pets'
        ordering = ['name']

    def __str__(self):
        return "{0}".format(self.name)

class cita (models.Model):
    pk_cita = models.AutoField(primary_key=True, null=False, blank=False)
    fecha = models.CharField(max_length=50, null=False, blank=False)
    fk_pet = models.ForeignKey(pet, null=False, blank=False, on_delete=models.CASCADE)
    fk_petshop = models.ForeignKey(petshop, null=False, blank=False, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'cita'
        verbose_name_plural = 'citas'
        ordering = ['fecha']

    def __str__(self):
        return "{0}".format(self.fecha)

