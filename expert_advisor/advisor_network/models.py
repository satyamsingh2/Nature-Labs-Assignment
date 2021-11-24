from django.db.models import Model, CharField, EmailField, ForeignKey, DateTimeField, CASCADE
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    name = CharField(max_length=100)
    email = EmailField(unique=True)

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return f"User(id={self.id}, username={self.get_username()})"


class Advisor(Model):
    name = CharField(max_length=100)
    image_url = CharField(max_length=1024)

    class Meta:
        verbose_name = "Advisor"
        verbose_name_plural = "Advisors"

    def __str__(self):
        return f'{self.name}'

class Booking(Model):
    user = ForeignKey(User, on_delete=CASCADE)
    advisor = ForeignKey(Advisor, on_delete=CASCADE)
    booking_time = DateTimeField()

    class Meta:
        verbose_name = "Booking"
        verbose_name_plural = "Bookings"


