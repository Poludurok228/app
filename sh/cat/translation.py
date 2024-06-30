from modeltranslation.translator import register, TranslationOptions
from .models import AsicDescription, Property


@register(AsicDescription)
class AsicDescriptionTranslationOptions(TranslationOptions):
    fields = ('our', 'el', 'protect', 'firm', )


@register(Property)
class PropertyTranslationOptions(TranslationOptions):
    fields = ('power', 'cold', )
