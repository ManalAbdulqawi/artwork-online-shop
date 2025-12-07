from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Category(models.Model):
    class Meta:
        verbose_name_plural = "Categories"

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey(
        "Category", null=True, blank=True, on_delete=models.SET_NULL
    )
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    size = models.CharField(max_length=254)
    original_art = models.URLField(max_length=1024, null=True, blank=True)

    @property
    def first_image(self):
        return self.images.first()  # gets the first related Image object

    def __str__(self):
        return self.name


class Image(models.Model):
    product = models.ForeignKey(
        "Product", on_delete=models.CASCADE, related_name="images"
    )
    name = models.CharField(max_length=254)
    image = models.ImageField("image")

    def __str__(self):
        return self.name


class Watchlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="watchlist")
    product = models.ForeignKey(
        "Product", on_delete=models.CASCADE, related_name="watched_by"
    )
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("user", "product")  # Prevent duplicates

    def __str__(self):
        return f"{self.user.username} watches {self.product.name}"
