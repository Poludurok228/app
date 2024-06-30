from django.contrib import admin
from .models import *
from modeltranslation.admin import TranslationAdmin


@admin.register(AsicBrand)
class AsicBrandAdmin(admin.ModelAdmin):
    list_display = ('title', )
    prepopulated_fields = {"slug": ("title",)}


@admin.register(FastFilter)
class AsicBrandAdmin(admin.ModelAdmin):
    list_display = ('title', )
    prepopulated_fields = {"slug": ("title",)}


@admin.register(Asic)
class AsicBrandAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'usdt', 'brand', 'hesh', 'active', 'availability', 'popular', 'asic_number', 'title_min')
    list_filter = ('title', 'price', 'brand', 'active', 'asic_number')
    list_editable = ('active', 'availability', 'usdt', 'price', 'popular', 'asic_number', 'title_min')
    prepopulated_fields = {"slug": ("title",)}


@admin.register(Stabilizer)
class StabilizerAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'brand')
    list_filter = ('title', 'price', 'brand')
    list_editable = ('price',)
    prepopulated_fields = {"slug": ("title",)}


@admin.register(StabilizerBrand)
class StabilizerBrandAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_filter = ('title',)
    prepopulated_fields = {"slug": ("title",)}


@admin.register(Phase)
class PhaseAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_filter = ('title',)
    prepopulated_fields = {"slug": ("title",)}


@admin.register(AsicDescription)
class AsicDescriptionTranslationOptions(TranslationAdmin):
    list_display = ('title', 'id', )
    list_display_links = ('title',)


@admin.register(Property)
class PropertyTranslationOptions(TranslationAdmin):
    list_display = ('title', 'id', )
    list_display_links = ('title',)


admin.site.register(MiniProperty)
admin.site.register(Coin)
admin.site.register(AsicDetailPhoto)
admin.site.register(AsicPopularBg)
admin.site.register(StabilizerProperty)
admin.site.register(StabilizerImage)
