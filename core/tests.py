# -*- coding: utf-8 -*-
from django.test import TestCase


class HomepageTest(TestCase):
    def setUp(self):
        self.res = self.client.get('/')

    def test_get(self):
        'GET / must return status code 200'
        self.assertEqual(200, self.res.status_code)

    def test_template(self):
        'Homepage must use template index.html'
        self.assertTemplateUsed(self.res, 'index.html')
