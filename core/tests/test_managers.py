# -*- coding: utf-8 -*-
from django.test import TestCase
from core.models import Speaker, Contact, Talk


class ContactManagerTest(TestCase):
    def setUp(self):
        s = Speaker.objects.create(name='Jeferson Calazans',
            slug='jeferson-calazans', url='http://about.me/calazans10',
            description='Passionate software developer!')

        s.contact_set.add(Contact(kind='E', value='calazans10@gmail.com'),
                          Contact(kind='P', value='21-86478151'),
                          Contact(kind='F', value='21-33578819'))

    def test_emails(self):
        qs = Contact.emails.all()
        expected = ['<Contact: calazans10@gmail.com>']
        self.assertQuerysetEqual(qs, expected)

    def test_phones(self):
        qs = Contact.phones.all()
        expected = ['<Contact: 21-86478151>']
        self.assertQuerysetEqual(qs, expected)

    def test_faxes(self):
        qs = Contact.faxes.all()
        expected = ['<Contact: 21-33578819>']
        self.assertQuerysetEqual(qs, expected)


class PeriodManagerTest(TestCase):
    def setUp(self):
        Talk.objects.create(title='Morning Talk', start_time='10:00')
        Talk.objects.create(title='Afternoon Talk', start_time='12:00')

    def test_morning(self):
        'Should return only talks before 12:00.'
        self.assertQuerysetEqual(Talk.objects.at_morning(), ['Morning Talk'],
            lambda t: t.title)

    def test_afternoon(self):
        'Should return only talks after 11:59:59.'
        self.assertQuerysetEqual(Talk.objects.at_afternoon(), ['Afternoon Talk'],
            lambda t: t.title)
