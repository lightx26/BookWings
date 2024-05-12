from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, phone_number, email, first_name, last_name, gender, password=None):
        if not phone_number:
            raise ValueError('Users must have a phone number')

        user = self.model(
            phone_number=phone_number,
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            gender=gender
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, email, first_name, last_name, gender, password):
        user = self.create_user(phone_number, email, first_name, last_name, gender, password)
        user.is_admin = True
        user.save(using=self._db)
        return user


# Create your models here.
class CustomerRank(models.IntegerChoices):
    BRONZE = 0, 'Bronze'
    SILVER = 1, 'Silver'
    GOLD = 2, 'Gold'
    PLATINUM = 3, 'Platinum'
    DIAMOND = 4, 'Diamond'


class CustomerRankConditions:
    RANK_ORDER_CONDITIONS = {
        CustomerRank.SILVER: 20,
        CustomerRank.GOLD: 80,
        CustomerRank.PLATINUM: 150,
        CustomerRank.DIAMOND: 300
    }

    RANK_SPENT_CONDITIONS = {
        CustomerRank.SILVER: 500,
        CustomerRank.GOLD: 1000,
        CustomerRank.PLATINUM: 1500,
        CustomerRank.DIAMOND: 2000
    }


class User(AbstractBaseUser):
    first_name = models.CharField(max_length=20, blank=True)
    last_name = models.CharField(max_length=40, blank=True)

    phone_number = models.CharField(max_length=20, blank=False, unique=True)
    email = models.EmailField(max_length=255, blank=False, unique=True)
    gender = models.BooleanField(default=True)

    rank = models.IntegerField(default=CustomerRank.BRONZE, choices=CustomerRank.choices)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)

    @property
    def is_staff(self):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin

    @is_staff.setter
    def is_staff(self, value):
        self._is_staff = value

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'email', 'gender']

    objects = UserManager()

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'


class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    local_address = models.CharField(max_length=255)  # No. 120, Street 271 or Mango Pagoda, 3rd Floor
    commune = models.CharField(max_length=255)
    district = models.CharField(max_length=255)
    province = models.CharField(max_length=255)
