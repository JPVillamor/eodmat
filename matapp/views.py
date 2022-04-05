import mimetypes
from django.shortcuts import render, redirect
from django.http import HttpResponse

import csv

# Create your views here.
def index(request):
    return render(request, 'index.html', context={'text': 'Hello World'})

def home(request):
    return render(request, 'home.html')

def force_setup(request):
    return render(request, 'force_setup.html') 

def chart_js(request):
    return HttpResponse(request,'chart.js', content_type='text/javascript')


def exportcsv(request):
    records = Record.objects.all()
    response = HttpResponse('text/csv')
    response['Content-Disposition'] = 'attachment; filename=readings_' + User.objects.get(id=1).name + '.csv'
    writer = csv.writer(response)
    writer.writerow(['ID', 'Timestamp', 'Data', 'Tool'])
    recs = records.values_list('id', 'timestamp', 'data_value', 'tool_used')
    
    for rec in recs:
        writer.writerow(rec)
    
    return response

def getname(request):
	if request.method == 'POST':
		if request.POST.get('fname'):
			
			fname = request.POST['fname']
			u = UserInfo(name = fname)
			u.pk = 1
			u.save()
			#NewUser = User(u.name, 'brick', 'jackhammer')
			#NewUser.pk = 1
			#NewUser.save()
			return render(request, 'index.html')
		else:
		    return render(request, 'index.html')

