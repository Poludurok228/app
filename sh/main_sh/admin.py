from django.contrib import admin
from .models import *
from modeltranslation.admin import TranslationAdmin


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('title', )
    prepopulated_fields = {'slug': ('order_number',)}


@admin.register(TrustSteps)
class AsicDescriptionTranslationOptions(TranslationAdmin):
    list_display = ('id', 'description', )
    list_display_links = ('id',)


@admin.register(Slide)
class SlideTranslationOptions(TranslationAdmin):
    list_display = ('title', 'number', 'main_page', 'id')
    list_editable = ('number', 'main_page')
    prepopulated_fields = {'slug': ('title',)}
    list_display_links = ('id',)


@admin.register(BlogParagraph)
class BlogParagraphTranslationOptions(TranslationAdmin):
    list_display = ('title', 'id', )
    list_display_links = ('id',)


@admin.register(BlogTag)
class BlogTagTranslationOptions(TranslationAdmin):
    list_display = ('title', 'id')
    prepopulated_fields = {'slug': ('title',)}
    list_display_links = ('id',)


@admin.register(BlogNews)
class BlogNewsTranslationOptions(TranslationAdmin):
    list_display = ('title', 'publish', 'created', 'id')
    list_editable = ('publish',)
    prepopulated_fields = {'slug': ('title',)}
    list_display_links = ('title',)


@admin.register(AboutSteps)
class AboutStepsTranslationOptions(TranslationAdmin):
    list_display = ('title', 'id', )
    list_display_links = ('id',)


@admin.register(OrderSteps)
class OrderStepsTranslationOptions(TranslationAdmin):
    list_display = ('title', 'id', )
    list_display_links = ('id',)


@admin.register(Contracts)
class ContractsTranslationOptions(TranslationAdmin):
    list_display = ('title', )


@admin.register(ContractParagraph)
class ContractParagraphTranslationOptions(TranslationAdmin):
    list_display = ('title', )


@admin.register(ContractParagraphPoint)
class ContractParagraphPointTranslationOptions(TranslationAdmin):
    list_display = ('number', )


admin.site.register(Reviews)
admin.site.register(SvgImgSlide)
admin.site.register(OrderLot)
admin.site.register(Warranty)
admin.site.register(PhotoLocation)
admin.site.register(Shipping)
admin.site.register(Application)
admin.site.register(UploadFile)

