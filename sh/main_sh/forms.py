from django import forms
from django.utils.translation import gettext_lazy as _


class CodForm1(forms.Form):
    name = forms.CharField(label='', max_length=100, widget=forms.TextInput(
        attrs={'placeholder': _('Имя')}
    ))

    contact = forms.CharField(label='', max_length=150, widget=forms.TextInput(
        attrs={'placeholder': _('Контакты (номер телефона, tg аккаунт, whatsapp и тд.)')}
    ))


class CodForm2(forms.Form):
    name = forms.CharField(label='', max_length=100, widget=forms.TextInput(
        attrs={'placeholder': _('Имя')}
    ))

    contact = forms.CharField(label='', max_length=150, widget=forms.TextInput(
        attrs={'placeholder': _('Контакты (номер телефона, tg аккаунт, whatsapp и тд.)')}
    ))


class BlogForm(forms.Form):
    name = forms.CharField(label='', max_length=100, widget=forms.TextInput(
        attrs={'placeholder': _('Имя')}
    ))

    phone = forms.CharField(label='', max_length=150, widget=forms.TextInput(
        attrs={'placeholder': _('Телефон')}
    ))





