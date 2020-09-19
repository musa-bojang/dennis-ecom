from django.contrib import admin
from store.models import UserProfileInfo, User

# Register your models here.
from .models import*

admin.site.register(UserProfileInfo)
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)
