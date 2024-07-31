from django.db import models
from datetime import datetime
from config.utils import validate_image_extension


class AccountsModel(models.Model):
    CHOICES = [
        ('tashkent',"Toshkent"),
        ('andijan','Andijon'),
        ('fergana',"Farg'ona"),
        ('namangan',"Namangan"),
        ('sirdarya','Sirdaryo'),
        ('jizzax','Jizzax'),
        ('samarqand','Samarqand'),
        ('surxandarya',"Surxondaryo"),
        ('qashqadarya',"Qashqadaryo"),
        ('navoi','Navoiy'),
        ('buxoro','Buxoro'),
        ('xorazm','Xorazm'),
        ('qoraqalpogiston',"Qoraqalpog'iston")
   ]
    name = models.CharField(max_length = 65, default = "")
    surname = models.CharField(max_length = 65, default = "")
    birth = models.DateField(default = datetime.now )
    region = models.CharField(choices = CHOICES)
    phone_number = models.CharField(max_length = 13)
    email = models.EmailField()
    password = models.CharField(max_length = 255)
    otp = models.CharField(max_length = 6, default = "", blank = True)
    is_verified = models.BooleanField(default = False)
    image = models.ImageField(upload_to='profile/',blank=True, null=True,validators=[validate_image_extension],verbose_name="Profile image")

    class Meta:
        db_table = 'users'
        verbose_name = 'Foydalanuvchi'
        verbose_name_plural = 'Foydalanuvchilar'

    def __str__(self) -> str:
        return f'{self.name} {self.surname}'
