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
from selenium.webdriver.common.keys import Keys
import re


def index(request):
    driver = webdriver.Firefox()
    driver.get("https://www.zillow.com/homes/9091-Bobbie-Cir,-Huntington-Beach,-CA-92646_rb/")
    est_text = driver.find_elements_by_class_name("estimates")[0].text
    price_items = re.findall(r'\$(?:\d+\.)?\d+.\d+', est_text)
    est_price = price_items[0]
    est_rent = price_items[1]
    driver.close()
    return render(request, 'PropertyFinder/index.html',
     {
     'est_price': est_price, 
     'est_rent': est_rent
     }
     )

class DetailView(generic.DetailView):
    model = Question
    template_name = 'PropertyFinder/detail.html'
    print("shebar kjsdkanjd")
    def get_queryset(self):
    	return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'PropertyFinder/results.html'


def vote(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	try:
		selected_choice = question.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		return render(request, 'PropertyFinder/detail.html', {
			'question': question,
			'error_message': "You didn't select a choice.",
		})
	else:
		selected_choice.votes += 1
		selected_choice.save()
		return HttpResponseRedirect(reverse('PropertyFinder:results', args=(question.id,)))	