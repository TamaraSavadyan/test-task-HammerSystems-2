from django.db import models


class UserProfile(models.Model):
    phone_number = models.CharField(max_length=20, unique=True)
    auth_code = models.IntegerField()

    invite_code = models.OneToOneField('InviteCode', related_name='user_profile', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.phone_number


class InviteCode(models.Model):
    owner_code = models.CharField(max_length=6, unique=True)
    foreign_code = models.CharField(max_length=6, blank=True, null=True)
    is_owners_code_used = models.BooleanField(default=False)

    def __str__(self):
        return self.owner_code



'''
blank=True applies to form validation and allows the field to be empty in forms.
null=True applies to database schema and allows the field to have a NULL value in the database.
'''