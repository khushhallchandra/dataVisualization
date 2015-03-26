# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
import os.path
import json
import csv
from myproject.myapp.models import Document
from myproject.myapp.forms import DocumentForm

def list(request):
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile = request.FILES['docfile'])
            newdoc.save()
            return HttpResponseRedirect(reverse('myproject.myapp.views.list'))
    else:
        form = DocumentForm() # A empty, unbound form

    # Load documents for the list page
    documents = Document.objects.all()

    # Render list page with the documents and the form
    return render_to_response(
        'myapp/list.html',
        {'documents': documents, 'form': form},
        context_instance=RequestContext(request)
    )
def readData():
    completeName=os.path.join('myproject/media/documents/', 'a.csv') 
    d=[]
    f = open( completeName, 'r' )
	#data is assumed in the form of x and y values which are seperated by comma.
    csv_f = csv.reader(f)
    for row in csv_f:
    	row = [int(i) for i in row]
    	d.append(row)
    sorted_data=sorted(d,key=lambda tup: tup[1],reverse=True)
    data=[]
    for line in sorted_data:
        temp_dict={"name":line[0] , "data":line[1]}
        data.append(temp_dict)
    f.close()
    return data

def makeGraph(request):
    data=readData()
    print (data)
    return render_to_response('myapp/plot.html', {"obj_as_json": json.dumps(data)})
