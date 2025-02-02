from django.contrib import admin
from .models import *


@admin.register(WalletUSDT)
class WalletAdmin(admin.ModelAdmin):
    list_display = ('title', )
    prepopulated_fields = {'slug': ('title',)}
