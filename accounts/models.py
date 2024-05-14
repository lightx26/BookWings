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
        user.role = UserRole.ADMIN
        user.rank = None
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
        CustomerRank.SILVER: 10,
        CustomerRank.GOLD: 30,
        CustomerRank.PLATINUM: 100,
        CustomerRank.DIAMOND: 200
    }

    RANK_SPENT_CONDITIONS = {
        CustomerRank.SILVER: 1000,
        CustomerRank.GOLD: 3500,
        CustomerRank.PLATINUM: 8000,
        CustomerRank.DIAMOND: 15000
    }


class UserRole(models.TextChoices):
    CUSTOMER = 'CUSTOMER', 'Customer'
    DELIVERER = 'DELIVERER', 'Deliverer'
    ADMIN = 'ADMIN', 'Admin'


class User(AbstractBaseUser):
    phone_number = models.CharField(max_length=20, blank=False, unique=True)
    # __password__
    email = models.EmailField(max_length=255, blank=False, unique=True)

    first_name = models.CharField(max_length=20, blank=True)
    last_name = models.CharField(max_length=40, blank=True)
    gender = models.BooleanField(default=True)

    rank = models.IntegerField(default=CustomerRank.BRONZE, choices=CustomerRank.choices, null=True)

    date_joined = models.DateTimeField(auto_now_add=True)
    role = models.CharField(max_length=20, choices=UserRole.choices, default=UserRole.CUSTOMER)

    @property
    def is_admin(self):
        return self.role == UserRole.ADMIN

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
    # Relationships
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # Attributes
    local_address = models.CharField(max_length=255)  # No. 120, Street 271 or Mango Pagoda, 3rd Floor
    commune = models.CharField(max_length=255)
    district = models.CharField(max_length=255)
    province = models.CharField(max_length=255)
