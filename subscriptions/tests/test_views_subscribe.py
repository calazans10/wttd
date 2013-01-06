from django.test import TestCase
from subscriptions.forms import SubscriptionForm


class SubscribeTest(TestCase):
    def setUp(self):
        self.res = self.client.get('/inscricao/')

    def test_get(self):
        'GET /inscricao/ must return status code 200'
        self.assertEqual(200, self.res.status_code)

    def test_template(self):
        'Response should be a rendered template.'
        self.assertTemplateUsed(self.res, 'subscriptions/subscription_form.html')

    def test_html(self):
        'Html must contains input controls'
        self.assertContains(self.res, '<form')
        self.assertContains(self.res, '<input', 6)
        self.assertContains(self.res, 'type="text"', 4)
        self.assertContains(self.res, 'type="submit"')

    def test_csrf(self):
        'Html must contain csrf token.'
        self.assertContains(self.res, 'csrfmiddlewaretoken')

    def test_has_form(self):
        'Context must have the subscription form.'
        form = self.res.context['form']
        self.assertIsInstance(form, SubscriptionForm)
