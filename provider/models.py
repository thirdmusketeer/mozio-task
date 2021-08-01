from django.db import models
from django.core.validators import RegexValidator


class Provider(models.Model):
    name = models.CharField(max_length=120, help_text="Provider name")
    email = models.EmailField(blank=False, null=False, unique=True)

    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits"
                                         " allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=False, null=False, unique=True,
                                    help_text="Provider phone number")
    language = models.CharField(max_length=60, help_text="Provider language")
    currency = models.CharField(max_length=10, default="USD")

    def __str__(self):
        return self.name


class ProviderServiceArea(models.Model):
    name = models.CharField(max_length=120, help_text="Provider service area name")
    provider = models.ForeignKey(
        "provider.Provider",
        on_delete=models.CASCADE,
        related_name="service_area_provider",
        null=False
    )
    price = models.PositiveIntegerField()
    polygon = models.JSONField()
