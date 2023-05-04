from django.db import models

# Create your models here.

class User(models.Model):
    username=models.CharField(max_length=120,unique=True)
    email=models.EmailField(unique=True)

    def __str__(self):
        return self.email

    @property
    def balance(self):
        if hasattr(self, 'account'):
            return self.account.balance
        return 0
#
#
class BankAccountType(models.Model):
    name = models.CharField(max_length=128)
    maximum_withdrawal_amount = models.DecimalField(decimal_places=2,max_digits=12)
#     # annual_interest_rate = models.DecimalField(
#     #     validators=[MinValueValidator(0), MaxValueValidator(100)],
#     #     decimal_places=2,
#     #     max_digits=5,
#     #     help_text='Interest rate from 0 - 100'
#     # )
#     # interest_calculation_per_year = models.PositiveSmallIntegerField(
#     #     validators=[MinValueValidator(1), MaxValueValidator(12)],
#     #     help_text='The number of times interest will be calculated per year'
#     # )
#
    def __str__(self):
        return self.name
#
#     # def calculate_interest(self, principal):
#     #     """
#     #     Calculate interest for each account type.
#     #
#     #     This uses a basic interest calculation formula
#     #     """
#     #     p = principal
#     #     r = self.annual_interest_rate
#     #     n = Decimal(self.interest_calculation_per_year)
#     #
#     #     # Basic Future Value formula to calculate interest
#     #     interest = (p * (1 + ((r/100) / n))) - p
#     #
#     #     return round(interest, 2)
#
#
class UserBankAccount(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    account_type = models.ForeignKey(BankAccountType,on_delete=models.CASCADE)
    account_no = models.PositiveIntegerField(unique=True)

    GENDER_CHOICE = (("0", "Male"),("1", "Female"))
    gender = models.CharField(max_length=1, choices=GENDER_CHOICE)
    birth_date = models.DateField(null=True, blank=True)
    balance = models.DecimalField(default=0,max_digits=12,decimal_places=2)

class UserAddress(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    street_address = models.CharField(max_length=512)
    city = models.CharField(max_length=256)
    postal_code = models.PositiveIntegerField()
    country = models.CharField(max_length=256)

    def __str__(self):
        return self.user.email
