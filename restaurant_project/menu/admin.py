
# Register your models here.
from django.contrib import admin
from .models import MenuCategory, MenuItem, RestaurantInfo

class MenuItemInline(admin.TabularInline):
    model = MenuItem
    extra = 1
    fields = ('name', 'price', 'description', 'is_spicy', 'is_vegetarian', 'order')
    show_change_link = True

@admin.register(MenuCategory)
class MenuCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'order', 'item_count')
    list_editable = ('order',)
    search_fields = ('name', 'description')
    inlines = [MenuItemInline]
    
    def item_count(self, obj):
        return obj.items.count()
    item_count.short_description = 'Items'

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'is_spicy', 'is_vegetarian', 'order')
    list_filter = ('category', 'is_spicy', 'is_vegetarian')
    list_editable = ('price', 'is_spicy', 'is_vegetarian', 'order')
    search_fields = ('name', 'description')
    list_per_page = 20
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('category', 'name', 'description', 'price')
        }),
        ('Dietary Information', {
            'fields': ('is_spicy', 'is_vegetarian'),
            'classes': ('wide',)
        }),
        ('Display Order', {
            'fields': ('order',),
            'classes': ('collapse',)
        }),
    )

@admin.register(RestaurantInfo)
class RestaurantInfoAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'get_hours_summary')
    
    fieldsets = (
        ('Restaurant Details', {
            'fields': ('name', 'address', 'phone', 'email')
        }),
        ('Hours of Operation', {
            'fields': ('hours_weekday', 'hours_saturday', 'hours_sunday'),
            'description': 'Enter hours in format: "11:30 AM - 10:00 PM"'
        }),
    )
    
    def get_hours_summary(self, obj):
        return f"Weekdays: {obj.hours_weekday}"
    get_hours_summary.short_description = 'Hours Summary'
    
    def has_add_permission(self, request):
        # Allow only one RestaurantInfo instance
        if RestaurantInfo.objects.exists():
            return False
        return True