from django.db import models
from django.utils.text import slugify

class MenuCategory(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)  # Add this line
    description = models.TextField(blank=True)
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['order']
        verbose_name_plural = "Menu Categories"
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name

class MenuItem(models.Model):
    category = models.ForeignKey(MenuCategory, on_delete=models.CASCADE, related_name='items')
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    is_spicy = models.BooleanField(default=False)
    is_vegetarian = models.BooleanField(default=False)
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['order']
    
    def __str__(self):
        return self.name

class RestaurantInfo(models.Model):
    name = models.CharField(max_length=200, default="Le Bistro")
    address = models.TextField()
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    hours_weekday = models.CharField(max_length=100, help_text="Mon-Fri hours")
    hours_saturday = models.CharField(max_length=100)
    hours_sunday = models.CharField(max_length=100)
    
    class Meta:
        verbose_name_plural = "Restaurant Information"
    
    def __str__(self):
        return self.name