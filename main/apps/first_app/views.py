# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from django.views.decorators.csrf import csrf_exempt

import json
# NOTE: put all views as a class
# Create your views here.
# @csrf_exempt
def index(request):
    print('haha----\n', request)
    print(request.method)
    print(request.POST['bar'])
    data = {'val1' : 'this is x', 'val2' : True}
    return HttpResponse(json.dumps(data))
