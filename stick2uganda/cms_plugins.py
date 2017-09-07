from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext as _

from stick2uganda.models import Stick2UgandaPlugin


class Stick2UgandaProjectPlugin(CMSPluginBase):
    model = Stick2UgandaPlugin
    module = _("Stick2Uganda")
    name = _("Project Plugin")
    render_template = "stick2uganda/index.html"

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context

plugin_pool.register_plugin(Stick2UgandaProjectPlugin)