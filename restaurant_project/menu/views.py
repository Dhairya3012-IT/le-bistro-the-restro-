# Create your views here.
from django.shortcuts import render
from .models import MenuCategory, MenuItem, RestaurantInfo

def home(request):
    restaurant = RestaurantInfo.objects.first()
    return render(request, 'home.html', {'restaurant': restaurant})

def appetizers(request):
    category = MenuCategory.objects.filter(name__icontains='Appetizer').first()
    items = MenuItem.objects.filter(category=category) if category else []
    return render(request, 'appetizers.html', {'items': items})

def main_courses(request):
    category = MenuCategory.objects.filter(name__icontains='Main').first()
    items = MenuItem.objects.filter(category=category) if category else []
    return render(request, 'main_courses.html', {'items': items})

def desserts_drinks(request):
    dessert_category = MenuCategory.objects.filter(name__icontains='Dessert').first()
    drink_category = MenuCategory.objects.filter(name__icontains='Drink').first()
    
    desserts = MenuItem.objects.filter(category=dessert_category) if dessert_category else []
    drinks = MenuItem.objects.filter(category=drink_category) if drink_category else []
    
    return render(request, 'desserts_drinks.html', {
        'desserts': desserts,
        'drinks': drinks
    })

def hours_location(request):
    restaurant = RestaurantInfo.objects.first()
    return render(request, 'hours_location.html', {'restaurant': restaurant})