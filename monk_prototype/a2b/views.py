from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import urllib2
import json
from models import Stop
from forms import FromStop

# Create your views here.

def update_stops(request):
	"updates list of stops from OTP server."
	#remove hard-coding URL
	response = urllib2.urlopen('http://localhost:8080/otp/routers/default/index/stops')
	stop_data = json.load(response)

	#bulk_create might be faster
	if stop_data:
		for stop in stop_data:
			Stop.objects.update_or_create(**stop)

		return HttpResponseRedirect('success/')

	else: 
		return HttpResponseRedirect('error/')

def update_success(request):
	return HttpResponse('Stop list updated!')

def update_error(request):
	return HttpResponse('Error. No stop list found.')

def search_routes(request):
	form = FromStop()
	return render(request,'a2b/search_routes.html',{'form': form})

