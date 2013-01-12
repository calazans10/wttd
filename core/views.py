# -*- coding: utf-8 -*-
# from django.http import HttpResponse
from django.views.generic.simple import direct_to_template
from core.models import Speaker
from django.shortcuts import get_object_or_404


def homepage(request):
    return direct_to_template(request, template='index.html')


def speaker_detail(request, slug):
    speaker = get_object_or_404(Speaker, slug=slug)
    context = {'speaker': speaker}
    return direct_to_template(request, 'core/speaker_detail.html', context)
