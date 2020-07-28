from django.shortcuts import render

from datetime import datetime

from django.core.paginator import Paginator
# Create your views here.
from  django.http import HttpResponse
from django.db.models import Max , Sum , Avg , Min



import socket   

























def index(request):
    return render(request , 'temp/index.html' )





def yyy(request):

    HostName = socket.gethostname()                                                    
    Host_ip = socket.gethostbyname(HostName)                                   
    print("Your Hostname : ",HostName)                                                  
    print(" IP : ",Host_ip)  

    context = {'Host_ip':Host_ip , 'HostName':HostName}
    return render(request , 'temp/yyy.html' , context)
    


def ipmy(request):

    HostName = socket.gethostname()                                                    
    Host_ip = socket.gethostbyname(HostName)                                   
    print("Your Hostname : ",HostName)                                                  
    print(" IP : ",Host_ip)  

    context = {'Host_ip':Host_ip , 'HostName':HostName}
    return render(request , 'temp/ippp.html' , context)




























    