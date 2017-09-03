from django.shortcuts import render


def contact(request):
    template_name = 'themes/partials/contact.html'
    context = {

    }
    render(template_name, context)
