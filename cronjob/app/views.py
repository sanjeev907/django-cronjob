from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

import logging

logger = logging.getLogger(__name__)

def home(request):
    return HttpResponse("Django")
