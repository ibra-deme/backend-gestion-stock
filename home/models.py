from django.db import models

# Create your models here.
class Categorie(models.Model):
    name=models.CharField(max_length=200)
    description=models.CharField(max_length=200)

    def __str__(self):
        return self.name
class Client(models.Model):
    name= models.CharField(max_length=200)
    email=models.EmailField()
    phone=models.IntegerField()
    address=models.CharField(max_length=200)

    def __str__(self):
        return self.name 

class Fournisseur(models.Model):
    name= models.CharField(max_length=200)
    email=models.EmailField()
    phone=models.IntegerField()
    address=models.CharField(max_length=200)

    def __str__(self):
        return self.name 
    

class Produit(models.Model):
    name=models.CharField(max_length=200)
    quantite=models.IntegerField()
    description=models.CharField(max_length=200)
    prix=models.IntegerField()
    image=models.ImageField()   
    categorie=models.ForeignKey(Categorie,blank=True,on_delete=models.CASCADE)
    fournisseur=models.ForeignKey(Fournisseur,blank=True,on_delete=models.CASCADE)

    def __str__(self):
        return self.name 