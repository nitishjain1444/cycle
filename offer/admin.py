from django.contrib import admin
from .models import Banner

class BannerAdmin(admin.ModelAdmin):
    list_display = ['heading','discription','image']

admin.site.register(Banner, BannerAdmin)
# Register your models here.
