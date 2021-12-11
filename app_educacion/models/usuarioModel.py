from django.db import models
from django.contrib.auth.models  import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.contrib.auth.hashers import make_password

# Manager to handle type of DjangoUsers, not the same as ApplicationRoles.
class UserManager(BaseUserManager):
    def create_user(self, cedula, password=None):
        if not cedula:
            raise ValueError("El cliente debe tener una cedula.")
        user = self.model(cedula=cedula)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, cedula, password):
        user = self.create_user(
            cedula = cedula, 
            password = password
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    #   ======================== OJO CON LA COMA AL FINAL   ========================
    id                       = models.BigAutoField(primary_key=True)
    cedula                   = models.CharField('Cedula', max_length=50, unique=True)
    nombre                   = models.CharField('Nombre',max_length=100)  
    correo_electronico       = models.CharField('Correo Electronico',max_length=100)
    direccion                = models.CharField('Direccion',max_length=250)
    password                 = models.CharField('Password',max_length=100) 
    departamento             = models.CharField('Deparatamento',max_length=100)  
    municipio_de_residencia  = models.CharField('Municipio de Residencia',max_length=100)
    perfil                   = models.CharField('Perfil',max_length=100) 
   
    
    def save(self, **kwargs):
        some_salt = 'mMUj0DrIK6vgtdIYepkIxN'
        self.password = make_password(self.password, some_salt)
        super().save(**kwargs)
    objects        = UserManager()
    USERNAME_FIELD = 'cedula'