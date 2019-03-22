from django.contrib import admin
from .models import (Product, Description, Extra_Info, Review, Comments, Images)

# Register your models here.
admin.site.register(Product)
admin.site.register(Description)
admin.site.register(Extra_Info)
admin.site.register(Review)
admin.site.register(Comments)
admin.site.register(Images)