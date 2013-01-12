# -*- coding: utf-8 -*-
from django.test import TestCase
from core.models import Speaker
from core.models import Contact
from django.core.exceptions import ValidationError


class SpeakerModelTest(TestCase):
    def setUp(self):
        self.speaker = Speaker(name='Jeferson Calazans',
                                slug='jeferson-calazans',
                                url='http://about.me/calazans10',
                                description='Passionate software developer!')
        self.speaker.save()

    def test_create(self):
        'Speaker instance should be saved'
        self.assertEqual(1, self.speaker.pk)

    def test_unicode(self):
        'Speaker string representation should be the name.'
        self.assertEqual(u'Jeferson Calazans', unicode(self.speaker))


class ContactModelTest(TestCase):
    def setUp(self):
        self.speaker = Speaker(name='Jeferson Calazans',
                                slug='jeferson-calazans',
                                url='http://about.me/calazans10',
                                description='Passionate software developer!')
        self.speaker.save()

    def test_email(self):
        contact = Contact.objects.create(speaker=self.speaker, kind='E',
            value='calazans10@gmail.com')
        self.assertEqual(1, contact.pk)

    def test_phone(self):
        contact = Contact.objects.create(speaker=self.speaker, kind='P',
            value='21-99995555')
        self.assertEqual(1, contact.pk)

    def test_fax(self):
        contact = Contact.objects.create(speaker=self.speaker, kind='F',
            value='21-66665555')
        self.assertEqual(1, contact.pk)

    def test_kind(self):
        'Contact kind should be limited to E, P or F.'
        contact = Contact(speaker=self.speaker, kind='A', value='B')
        self.assertRaises(ValidationError, contact.full_clean)
