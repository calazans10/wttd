# _*- coding: utf-8 -*-
from django.test import TestCase
from django.core.urlresolvers import reverse as r
from core.models import Speaker


class SpeakerDetailTest(TestCase):
    def setUp(self):
        Speaker.objects.create(name='Jeferson Calazans',
                                slug='jeferson-calazans',
                                url='http://about.me/calazans10',
                                description='Passionate software developer!')

        url = r('core:speaker_detail', kwargs={'slug': 'jeferson-calazans'})
        self.resp = self.client.get(url)

    def test_get(self):
        'GET should result in 200.'
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        'Template should be core/speaker_detail.html'
        self.assertTemplateUsed(self.resp, 'core/speaker_detail.html')

    def test_html(self):
        'Html must contain data.'
        self.assertContains(self.resp, 'Jeferson Calazans')
        self.assertContains(self.resp, 'Passionate software developer!')
        self.assertContains(self.resp, 'http://about.me/calazans10')

    def test_context(self):
        'Speaker must be in context.'
        speaker = self.resp.context['speaker']
        self.assertIsInstance(speaker, Speaker)


class SpeakerDetailNotFound(TestCase):
    def test_not_found(self):
        url = r('core:speaker_detail', kwargs={'slug': 'john-dee'})
        response = self.client.get(url)
        self.assertEqual(404, response.status_code)
