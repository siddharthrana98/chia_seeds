from django.contrib import admin
from .models import *

# Register your models here.
# class couponAdmin(admin.ModelAdmin):
#     list_display = ['code','valid_from','valid_to','discount','active']
#     list_filter = ['active','valid_from','valid_to']
#     search_fields = ['code']
     
admin.site.register(Offercard)
admin.site.register(Product)
admin.site.register(ProductReview)
admin.site.register(UserCart)
# admin.site.register(coupon)