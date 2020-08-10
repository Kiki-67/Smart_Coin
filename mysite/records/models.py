from django.db import models
from datetime import date
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

'''
 'Change your models (in models.py).\n'
 'Run python manage.py makemigrations to create migrations for those changes\n'
 'Run python manage.py migrate to apply those changes to the database.\n'
 'python manage.py migrate --run-syncdb')
'''


# Create your models here.
class UserProfile(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('W', 'Female')
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    gender = models.CharField(
        max_length=1,
        choices=GENDER_CHOICES,
        default='M',
    )

    def __str__(self):
        return " %s" % self.user.username


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class Expense(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.IntegerField(default=0)
    day = models.DateField(default=date.today)
    expense_type = models.CharField(
        max_length=50,
        default='Routine household maintain',
    )
    payment_method = models.CharField(
        max_length=20,
        default='Credit Card',
    )
    currency_type = models.CharField(
        max_length=10,
        default='USD',
    )
    amount_usd = models.IntegerField(default=0)

    def __str__(self):
        return "%s, %s, %s, %s" % (self.user, self.expense_type, self.amount, self.day)


class Income(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    currency_type = models.CharField(max_length=10, default='USD')
    amount = models.IntegerField(default=0)
    day = models.DateField(default=date.today)
    amount_usd = models.IntegerField(default=0)

    def __str__(self):
        return "%s, %s,%s, %s" % (self.user, self.amount, self.currency_type, self.day)


class Budget(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.IntegerField(default=0)
    day = models.DateField(default=date.today)
    currency_type = models.CharField(max_length=10, default='USD')
    amount_usd = models.IntegerField(default=0)

    def month_budget(self):
        return self.day.strftime('%B, %Y')
