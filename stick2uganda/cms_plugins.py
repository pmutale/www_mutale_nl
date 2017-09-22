from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext as _

from stick2uganda import models
from stick2uganda.models import Stick2UgandaPlugin


class Stick2UgandaProjectPlugin(CMSPluginBase):
    model = Stick2UgandaPlugin
    module = _("Stick2Uganda")
    name = _("Project Plugin")
    render_template = "stick2uganda/index.html"

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context


class ProjectImagePlugin(CMSPluginBase):
    model = models.S2UImagePlugin
    name = _('Add Project Image')
    render_template = 'stick2uganda/project/p_image.html'


plugin_pool.register_plugin(ProjectImagePlugin)
plugin_pool.register_plugin(Stick2UgandaProjectPlugin)

