from modeltranslation.translator import register, TranslationOptions
from .models import Slide, BlogParagraph, BlogTag, BlogNews, AboutSteps, TrustSteps, OrderSteps, ContractParagraph, Contracts, ContractParagraphPoint


@register(TrustSteps)
class AsicDescriptionTranslationOptions(TranslationOptions):
    fields = ('title', 'description', )


@register(Slide)
class SlideTranslationOptions(TranslationOptions):
    fields = ('title', 'description', )


@register(BlogParagraph)
class BlogParagraphTranslationOptions(TranslationOptions):
    fields = ('title', 'text', )


@register(BlogTag)
class BlogTagTranslationOptions(TranslationOptions):
    fields = ('title', )


@register(BlogNews)
class BlogNewsTranslationOptions(TranslationOptions):
    fields = ('title', 'description', )


@register(AboutSteps)
class AboutStepsTranslationOptions(TranslationOptions):
    fields = ('title', 'description', )


@register(OrderSteps)
class OrderStepsTranslationOptions(TranslationOptions):
    fields = ('title', 'description', )


@register(ContractParagraph)
class ContractParagraphTranslationOptions(TranslationOptions):
    fields = ('title', )


@register(Contracts)
class ContractsTranslationOptions(TranslationOptions):
    fields = ('title', )


@register(ContractParagraphPoint)
class ContractParagraphPointTranslationOptions(TranslationOptions):
    fields = ('text', )

