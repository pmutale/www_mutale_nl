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
    cache = False

    def render(self, context, instance, placeholder):
        context = super(ContactPlugin, self).render(context, instance, placeholder)
        return context


class ComingSoonPlugin(CMSPluginBase):
    model = models.ComingSoon
    name = _("ComingSoon")
    render_template = "themes/partials/coming_soon.html"
    cache = False

    def render(self, context, instance, placeholder):
        context = super(ComingSoonPlugin, self).render(context, instance, placeholder)
        request = context['request']
        if request.method == 'POST':
            form = forms.Subscribe(request.POST, request)

            if form.is_valid():
                context.update({
                    'thanks': True,
                    'instance': instance
                })

                email_content = Context({
                    'email': form.cleaned_data['email'],
                })

                plain = get_template('themes/email/contactform.txt')
                html = get_template('themes/email/contactform.html')

                subject = 'Website subscriber'
                from_email = 'Webmaster P.Mutale <webmaster@mutale.nl>'
                recepients = ['peter@mutale.nl', ]

                text_content = plain.render(email_content)
                html_content = html.render(email_content)

                email = EmailMultiAlternatives(subject, text_content, from_email, recepients)
                email.attach_alternative(html_content, 'text/html')
                email.send()
            else:
                context.update({
                    'instance': instance,
                    'form': form
                })
        else:
            context.update({
                'instance': instance,
                'form': forms.Subscribe(),
                'thanks': False,
            })
        return context

plugin_pool.register_plugin(ContactPlugin)
plugin_pool.register_plugin(ComingSoonPlugin)
