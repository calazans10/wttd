# -*- coding: utf-8 -*-
# from django.http import HttpResponse
# from django.template import loader, Context
# from django.conf import settings
# from django.shortcuts import render_to_response
# from django.template import RequestContext
from django.views.generic.simple import direct_to_template


def homepage(request):
    return direct_to_template(request, template='index.html')
    # context = RequestContext(request)
    # return render_to_response('index.html', context)

    # context = {'STATIC_URL': settings.STATIC_URL}
    # t = loader.get_template('index.html')
    # c = Context()
    # content = t.render(c)

    # return HttpResponse(content)
