# -*- coding: utf-8 -*-
from django import forms
from .models import Subscription
# from django.utils.translation import gettext as _


class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscription
        exclude = ('paid',)
    # name = forms.CharField(label=_('Name'))
    # cpf = forms.CharField(label=_('CPF'))
    # email = forms.EmailField(label=_('Email'))
    # phone = forms.CharField(label=_('Telefone'))
