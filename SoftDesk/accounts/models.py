from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.utils import timezone


class CustomUser(AbstractUser):
    can_be_contacted = models.BooleanField(default=False)
    can_data_be_shared = models.BooleanField(default=False)
    date_of_birth = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        if self.date_of_birth:
            self.validate_age()
        super().save(*args, **kwargs)

    def validate_age(self):
        age = timezone.now().year - self.date_of_birth.year
        if age < 15:
            raise ValidationError("You must be at least 15 years old to register.")
