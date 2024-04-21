from django.db import models


class UserProfile(models.Model):
    phone_number = models.CharField(max_length=20, unique=True)
    auth_code = models.IntegerField()

    def __str__(self):
        return self.phone_number
