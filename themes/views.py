from django.shortcuts import render


def contact(request):
    template_name = 'themes/partials/contact.html'
    context = {

    }
    render(request, template_name, context)
