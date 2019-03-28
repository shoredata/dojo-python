# coding: utf-8

from __future__ import absolute_import, unicode_literals

from django.contrib.auth.models import User
from django.template import Context, RequestContext, Template
from django.test import TestCase, override_settings

from ..base import BaseTestCase
from ..models import NonAsciiRepr


class TemplatesPanelTestCase(BaseTestCase):

    def setUp(self):
        super(TemplatesPanelTestCase, self).setUp()
        self.panel = self.toolbar.get_panel_by_id('TemplatesPanel')
        self.panel.enable_instrumentation()
        self.sql_panel = self.toolbar.get_panel_by_id('SQLPanel')
        self.sql_panel.enable_instrumentation()

    def tearDown(self):
        self.sql_panel.disable_instrumentation()
        self.panel.disable_instrumentation()
        super(TemplatesPanelTestCase, self).tearDown()

    def test_queryset_hook(self):
        t = Template("No context variables here!")
        c = Context({
            'queryset': User.objects.all(),
            'deep_queryset': {
                'queryset': User.objects.all(),
            }
        })
        t.render(c)

        # ensure the query was NOT logged
        self.assertEqual(len(self.sql_panel._queries), 0)

        ctx = self.panel.templates[0]['context'][1]
        self.assertIn('<<queryset of auth.User>>', ctx)
        self.assertIn('<<triggers database query>>', ctx)

    def test_object_with_non_ascii_repr_in_context(self):
        self.panel.process_request(self.request)
        t = Template("{{ object }}")
        c = Context({'object': NonAsciiRepr()})
        t.render(c)
        self.panel.process_response(self.request, self.response)
        self.panel.generate_stats(self.request, self.response)
        self.assertIn('nôt åscíì', self.panel.content)

    def test_insert_content(self):
        """
        Test that the panel only inserts content after generate_stats and
        not the process_response.
        """
        t = Template("{{ object }}")
        c = Context({'object': NonAsciiRepr()})
        t.render(c)
        self.panel.process_response(self.request, self.response)
        # ensure the panel does not have content yet.
        self.assertNotIn('nôt åscíì', self.panel.content)
        self.panel.generate_stats(self.request, self.response)
        # ensure the panel renders correctly.
        self.assertIn('nôt åscíì', self.panel.content)
        self.assertValidHTML(self.panel.content)

    def test_custom_context_processor(self):
        self.panel.process_request(self.request)
        t = Template("{{ content }}")
        c = RequestContext(self.request, processors=[context_processor])
        t.render(c)
        self.panel.process_response(self.request, self.response)
        self.panel.generate_stats(self.request, self.response)
        self.assertIn('tests.panels.test_template.context_processor', self.panel.content)

    def test_disabled(self):
        config = {
            'DISABLE_PANELS': {'debug_toolbar.panels.templates.TemplatesPanel'}
        }
        self.assertTrue(self.panel.enabled)
        with self.settings(DEBUG_TOOLBAR_CONFIG=config):
            self.assertFalse(self.panel.enabled)


@override_settings(DEBUG=True,
                   DEBUG_TOOLBAR_PANELS=['debug_toolbar.panels.templates.TemplatesPanel'])
class JinjaTemplateTestCase(TestCase):
    def test_django_jinja2(self):
        r = self.client.get('/regular_jinja/foobar/')
        self.assertContains(r, 'Test for foobar (Jinja)')
        self.assertContains(r, '<h3>Templates (1 rendered)</h3>')
        self.assertContains(r, '<small>jinja2/basic.jinja</small>')


def context_processor(request):
    return {'content': 'set by processor'}
