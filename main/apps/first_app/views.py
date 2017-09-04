# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

import json

# Create your views here.
def index(request):
    data = {'val1' : 'this is x', 'val2' : True}
    return HttpResponse(json.dumps(data))
