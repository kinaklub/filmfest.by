from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from cms.models.pluginmodel import CMSPlugin

from django.utils.translation import ugettext_lazy as _

from .models import ContactPluginModel

class ContactPlugin(CMSPluginBase):
    model = ContactPluginModel
    name = _("CPM Contact Plugin")
    render_template = "contact_plugin.html"

    def render(self, context, instance, placeholder):
        context['instance'] = instance
        return context

plugin_pool.register_plugin(ContactPlugin);


