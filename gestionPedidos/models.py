from django.db import models

# Create your models here.

#Se crea una clase por cada tabla en al abse de datos

class Clientes(models.Model): #Primera Tabla / Para trabajar con base de datos en Python se necesita trabajar con Model
    nombre = models.CharField(max_length=30)
    direccion = models.CharField(max_length=50, verbose_name="La dirección") #En el panel de administración el nombre cambia
    email = models.EmailField(blank=True, null=True) #Formato Email /En el panel de administración el campo no será obligatorio
    tfno = models.CharField(max_length=7)
    
    #def __str__(self):
    #    return self.nombre
    
    
class Articulos(models.Model): #Segunda Tabla
    nombre = models.CharField(max_length=30)
    seccion = models.CharField(max_length=20)
    precio = models.IntegerField()
    
    def __str__(self):
        return "El nombre es %s la seccion es %s y el precio es %s" %(self.nombre, self.seccion, self.precio)
    
class Pedidos(models.Model): #Tercera Tabla
    numero = models.IntegerField()
    fecha = models.DateField()
    entregado = models.BooleanField()
    
    
    
    
class Pedidos(models.Model): #Tercera Tabla
    numero = models.IntegerField()
    fecha = models.DateField()
    entregado = models.BooleanField()
    
    