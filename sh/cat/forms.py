from django import forms
from django.utils.translation import gettext_lazy as _


class TabsForm(forms.Form):
    name = forms.CharField(label='', max_length=100, widget=forms.TextInput(
        attrs={'placeholder': _('Имя')}
    ))
    phone = forms.CharField(label='', max_length=100, widget=forms.TextInput(
        attrs={'placeholder': _('Телефон')}
    ))


class QuestionAsicForm(forms.Form):
    name = forms.CharField(label='', max_length=100, widget=forms.TextInput(
        attrs={'placeholder': _('Ваше имя')}
    ))
    mail = forms.CharField(label='', max_length=100, widget=forms.EmailInput(
        attrs={'placeholder': _('Электронная почта')}
    ))
    contact = forms.CharField(label='', max_length=200, widget=forms.TextInput(
        attrs={'placeholder': _('Как с Вами связаться? (телефон, telegram, и тд)')}
    ))
    sub = forms.CharField(label='', max_length=100, widget=forms.TextInput(
        attrs={'placeholder': _('Тема сообщения')}
    ))
    message = forms.CharField(label='', max_length=1000, widget=forms.Textarea(
        attrs={'placeholder': _('Ваше сообщение')}
    ))


class OrderForm(forms.Form):
    name = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={
            'placeholder': _('Ваше имя'),
            'class': 'form-control'
        })
    )
    phone = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={
            'placeholder': '+(380) 99-999-99-99',
            'id': 'phone',
            'class': 'form-control'
        })
    )
    email = forms.EmailField(
        label='',
        required=False,
        widget=forms.EmailInput(attrs={
            'placeholder': 'example@mail.com',
            'class': 'form-control'
        })
    )
    telegram = forms.CharField(
        label='',
        required=False,
        widget=forms.TextInput(attrs={
            'placeholder': '@gpts_support',
            'class': 'form-control'
        })
    )
    quantity = forms.IntegerField(
        required=False,
        widget=forms.NumberInput(attrs={
            'id': 'quantity',
            'class': 'form-control',
            'value': '1'
        })
    )

    # Это поле необязательное если цена устанавливается динамически на фронтенде.
    price = forms.DecimalField(
        disabled=True,
        required=False,
        widget=forms.NumberInput(attrs={
            'class': 'totality_price',
            'value': '1',
            'class': 'form-control'
        })
    )
