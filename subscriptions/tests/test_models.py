# -*- coding: utf-8 -*-
from django.test import TestCase
from django.db import IntegrityError
from datetime import datetime
from subscriptions.models import Subscription


class SubscriptionTest(TestCase):
    def setUp(self):
        self.obj = Subscription(name='Jeferson Calazans', cpf='60546831524',
            email='calazans10@gmail.com', phone='21-86478151',)

    def test_create(self):
        'Subscription must have name, cpf, email, phone'
        self.obj.save()
        self.assertEqual(self.obj.id, 1)

    def test_has_created_at(self):
        'Subscription must have created_at'
        self.obj.save()
        self.assertIsInstance(self.obj.created_at, datetime)

    def test_unicode(self):
        self.assertEqual(u'Jeferson Calazans', unicode(self.obj))


class SubscriptionUniqueTest(TestCase):
    def setUp(self):
        # Create a first entry to force the colision
        Subscription.objects.create(name='Jeferson Calazans', cpf='60546831524',
            email='calazans10@gmail.com', phone='21-86478151',)

    def test_unique_cpf(self):
        'CPF must be unique'
        s = Subscription(name='Fulano de tal', cpf='60546831524',
            email='fulano@example.com', phone='21-88657495',)
        self.assertRaises(IntegrityError, s.save)

    def test_unique_email(self):
        s = Subscription(name='Fulano de tal', cpf='60546831529',
            email='calazans10@gmail.com', phone='21-88657495',)
        self.assertRaises(IntegrityError, s.save)
