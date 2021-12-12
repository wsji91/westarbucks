from django.db import models

# Create your models here.
class Menu(models.Model):
    name = models.CharField(max_length=20)
    
    class Meta:
        db_table = 'menus'

class Category(models.Model):
    name = models.CharField(max_length=20)
    menu = models.ForeignKey('Menu', on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'categories'
        
class Drink(models.Model):
    name = models.CharField(max_length=20)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    allergy = models.ManyToManyField('Allergy', through='Allergy_drink')
    
    class Meta:
        db_table = 'drinks'

class Allergy(models.Model):
    name = models.CharField(max_length=20, null=True)
    
    class Meta:
        db_table = 'allergies'

class Allergy_drink(models.Model):
    allergy = models.ForeignKey('Allergy', on_delete=models.CASCADE, null=True)
    drink = models.ForeignKey('Drink', on_delete=models.CASCADE, null=True)
    
    class Meta:
        db_table = 'allergies_drinks'

class Image(models.Model):
    image_url = models.TextField(max_length=2000, null=True)
    drink = models.ForeignKey('Drink', on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'images'

class Nutrition(models.Model):
    one_serving_kcal = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    sodium_mg = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    saturated_fat_g = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    sugars_g = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    protein_g = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    caffeine_g = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    drink = models.ForeignKey('Drink', on_delete=models.CASCADE)
    size = models.ForeignKey('Size', on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'nutritions'
        
        
class Size(models.Model):
    name = models.CharField(max_length=20)
    size_ml = models.CharField(max_length=20)
    size_fluid_ounce = models.CharField(max_length=20)
    
    class Meta:
        db_table = 'sizes'
    