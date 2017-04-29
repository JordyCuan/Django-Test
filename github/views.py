# -*- coding: utf-8 -*-
#from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from controllers import search_term_github


# Create your views here.
def index(request):
	context = search_term_github(request)
	return HttpResponse(render(request, 'index.html', context))