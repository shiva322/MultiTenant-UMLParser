# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
import os
import subprocess
from forms import ScoresForm
from models import Tenant,Scores

# Create your views here.
def home(request):
    return render(request, 'home.html')

def upload(request,tenant_id):
    return render(request, 'upload.html', {'what':'File upload Tenant'+tenant_id})

def uploadAction(request,tenant_id):
    if request.method == 'POST':
        handle_uploaded_file(request.FILES['file'], str(request.FILES['file']))
        global filename
        filename =  str(request.FILES['file']).split('.')[0]
        print filename
        subprocess.call(["pwd"])
        subprocess.call(["rm","-rf","source_code/","&&","mkdir","source_code"])
        subprocess.call(["unzip","-o","upload/"+str(request.FILES['file']), "-d","source_code/"])
        subprocess.call(["java","-jar","javaParser_ishan_en.jar","source_code/","uml-parser-"+filename+".png"])
        subprocess.call(["cp","uml-parser-"+filename+".png","static/."])
        subprocess.call(["ls"])
        return HttpResponseRedirect('/tenant'+tenant_id+'/result/')
    return HttpResponse("Failed")
 
def handle_uploaded_file(file, filename):
    if not os.path.exists('upload/'):
        os.mkdir('upload/')

    with open('upload/' + filename, 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)


def result(request,tenant_id):
    file = "uml-parser-"+filename+".png"
    if request.method == "POST":
        tenantDetails = Tenant.objects.get(pk=tenant_id)
        try:
            tenantScores = Scores.objects.get(tenant_id=tenant_id,test_case=filename)
        except:
            tenantScores = Scores.objects.create(tenant_id=tenant_id,test_case=filename)
        #tenantScores.test_case = filename
        form = ScoresForm(request.POST,instance=tenantScores)
        if form.is_valid():
            form.save()
        return render(request,'success.html',{'tenant':tenant_id})

    else:
        form = ScoresForm()
        return render(request,'result.html',{'imagefile':file,'form': form})

