# -*- coding: utf-8 -*-
from django.test import TestCase
from subscriptions.forms import SubscriptionForm


class SubscriptionFormTest(TestCase):
    def test_has_fields(self):
        'Form must have  4 fields'
        form = SubscriptionForm()
        self.assertItemsEqual(['name', 'email', 'cpf', 'phone'], form.fields)

    def test_cpf_is_digits(self):
        'CPF must only accept digits'
        form = self.make_validated_form(cpf='ABCDE99881')
        self.assertItemsEqual(['cpf'], form.errors)

    def test_cpf_has_11_digits(self):
        'CPF must have 11 digits'
        form = self.make_validated_form(cpf='1234')
        self.assertItemsEqual(['cpf'], form.errors)

    def test_email_is_option(self):
        'Email is optional'
        form = self.make_validated_form(email='')
        self.assertFalse(form.errors)

    def test_name_must_be_capitalized(self):
        'Name must be capitalized'
        form = self.make_validated_form(name='JEFERSON CALAZANS')
        self.assertEqual('Jeferson Calazans', form.cleaned_data['name'])

    def test_must_inform_email_or_phone(self):
        'Email and Phone are option, but one must be informed.'
        form = self.make_validated_form(email='', phone_0='', phone_1='')
        self.assertItemsEqual(['__all__'], form.errors)

    def make_validated_form(self, **kwargs):
        data = dict(name='Jeferson Calazans', email='jeferson@exemplo.com',
            cpf='12345678901', phone_0='21', phone_1='99887766',)
        data.update(kwargs)
        form = SubscriptionForm(data)
        form.is_valid()
        return form
