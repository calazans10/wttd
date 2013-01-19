# -*- coding: utf-8 -*-
from django.test import TestCase
from core.models import Talk
from core.managers import PeriodManager


class TalkModelTest(TestCase):
    def setUp(self):
        self.talk = Talk.objects.create(title=u'Introdução ao Django',
                                        description=u'Descrição da palestra.',
                                        start_time='10:00')

    def test_create(self):
        self.assertEqual(1, self.talk.pk)

    def test_unicode(self):
        self.assertEqual(u'Introdução ao Django', self.talk.title)

    def test_speakers(self):
        self.talk.speakers.create(name='Jeferson Calazans',
                                  slug='jeferson-calazans',
                                  url='http://abount.me/calazans10')
        self.assertEqual(1, self.talk.speakers.count())

    def test_period_manager(self):
        'Talk default manager must be instance of PeriodManager.'
        self.assertIsInstance(Talk.objects, PeriodManager)
