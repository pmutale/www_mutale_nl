from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.core.mail.message import EmailMultiAlternatives
from django.template import Context
from django.template.loader import get_template
from django.utils.translation import ugettext_lazy as _
from themes import models, forms


class ContactPlugin(CMSPluginBase):
    model = models.Contact
    name = _("Contact")
    render_template = "themes/partials/contact.html"
    cache = True

    def render(self, context, instance, placeholder):
        context = super(ContactPlugin, self).render(context, instance, placeholder)
        return context


class ComingSoonPlugin(CMSPluginBase):
    model = models.ComingSoon
    name = _("ComingSoon")
    render_template = "themes/partials/coming_soon.html"
    cache = True

    def render(self, context, instance, placeholder):
        context = super(ComingSoonPlugin, self).render(context, instance, placeholder)
        return context


plugin_pool.register_plugin(ContactPlugin)
plugin_pool.register_plugin(ComingSoonPlugin)
