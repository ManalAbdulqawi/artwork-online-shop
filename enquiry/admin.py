from django.contrib import admin
from .models import EnquiryRequest


# Register your models here.
@admin.register(EnquiryRequest)
class EnquiryRequestAdmin(admin.ModelAdmin):

    list_display = ('subject', 'message', 'read',)
