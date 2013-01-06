from django.test import TestCase
from subscriptions.models import Subscription


class SuccessTest(TestCase):
    def setUp(self):
        s = Subscription.objects.create(name='Jeferson Calazans', cpf='60546831524',
            email='calazans10@gmail.com', phone='21-86478151',)
        self.resp = self.client.get('/inscricao/%d/' % s.pk)

    def test_get(self):
        'GET /inscricao/1/ should return status 200'
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        'Uses template'
        self.assertTemplateUsed(self.resp, 'subscriptions/subscription_detail.html')

    def test_context(self):
        'Context must have a subscription instance'
        subscription = self.resp.context['subscription']
        self.assertIsInstance(subscription, Subscription)

    def test_html(self):
        'Check if subscription data was renderes.'
        self.assertContains(self.resp, 'Jeferson Calazans')


class SuccessNotFound(TestCase):
    def test_not_found(self):
        resp = self.client.get('/inscricao/0/')
        self.assertEqual(404, resp.status_code)
