from django.shortcuts import render, render_to_response
from django.template import RequestContext


def contact(request):
    template_name = 'themes/partials/contact.html'
    context = {

    }
    render(request, template_name, context)


def handler404(request):
    response = render_to_response('themes/error-pages/404.html', {})
    response.status_code = 404
    return response


def handler500(request):
    response = render_to_response('themes/error-pages/500.html', {})
    response.status_code = 500
    return response