# _*- coding: utf-8 -*-
from django.test import TestCase
from django.core.urlresolvers import reverse as r
from core.models import Talk


class TalkListDetailTest(TestCase):
    def setUp(self):
        t1 = Talk.objects.create(description=u'Descrição da palestra',
            title=u'Título da palestra', start_time='10:00')
        t1.speakers.create(name='Jeferson Calazans', slug='jeferson-calazans')

        self.resp = self.client.get(r('core:talk_detail', args=[1]))

    def test_get(self):
        'GET must result in 200'
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        'Uses template'
        self.assertTemplateUsed(self.resp, "core/talk_detail.html")

    def test_talk_in_context(self):
        talk = self.resp.context['talk']
        self.assertIsInstance(talk, Talk)

    def test_not_found(self):
        res = self.client.get(r('core:talk_detail', args=[0]))
        self.assertEqual(404, res.status_code)

    def test_html(self):
        self.assertContains(self.resp, u"Título da palestra")
        self.assertContains(self.resp, "palestrantes/jeferson-calazans/")
        self.assertContains(self.resp, "Jeferson Calazans")
