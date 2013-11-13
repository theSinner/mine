from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import Context
import datetime
def hello(request):
	now=datetime.datetime.now()
	return render_to_response('current_datetime.html',{'current_date':now})
def homeF(request):
	tileData=[]
	tileData.append(['contact','Contact Us'])
	tileData.append(['about','About Us'])
	tileData.append(['project','Projects'])
	tileData.append(['product','Products'])
	tileData.append(['home','Home'])
	vr={'num':len(tileData),'tda':tileData,'pic':36}
	return render_to_response('home.html',vr)
def catalog(request):
	return HttpResponse(open('cd_catalog.xml').read())
#	return render(request, 'cd_catalog.xml', {"foo": "bar"} content_type="application/xhtml+xml")
#	return HttpResponse("FUCK")
def about(request):
	return render_to_response('about.html',{});
