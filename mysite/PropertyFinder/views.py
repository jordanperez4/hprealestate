# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Choice, Question

from django.utils import timezone
from selenium import webdriver
from . import house_site_info


def index(request):
    search_text = "9091 Bobbie Cir, Huntington Beach, CA"
    driver = webdriver.Firefox()
    zillow_info = house_site_info.get_zillow_info(driver, search_text)
    realtor_info = house_site_info.get_realtor_info(driver, search_text)
    driver.close()
    return render(request, 'PropertyFinder/index.html',
         {
         'zillow_info': zillow_info,
         'realtor_info': realtor_info
         }
     )

