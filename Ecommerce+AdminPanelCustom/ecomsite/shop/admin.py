from django.contrib import admin
from .models import Product, Order
# Register your models here.

admin.site.site_header = "E-Commerce Site"
admin.site.site_title = "ABC Shopping"
admin.site.index_title = "Manage ABC Shopping"

class ProductAdmin(admin.ModelAdmin):

    def changeCategoryToDefault(self, request, queryset):
        queryset.update(category="default")

    changeCategoryToDefault.short_description = "Default Category"
    list_display = ('title', 'price', 'discount_price', 'category', 'description')
    search_fields = ('title', 'category', 'description')
    actions = ('changeCategoryToDefault',)
    fields = ('title', 'price', 'discount_price')
    list_editable = ('price', 'discount_price', )

    

admin.site.register(Product, ProductAdmin)
admin.site.register(Order)