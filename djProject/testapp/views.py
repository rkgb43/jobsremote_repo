from django.shortcuts import render
from testapp.models import *
from django.core.paginator import Paginator, PageNotAnInteger,EmptyPage

# Create your views here.
def index (request):
    return render(request,'testapp/index.html')

def hydjobs (request):
    job_list=hyjobs.objects.all()
    my_dict={'job_list': job_list}
    return render(request,'testapp/hydjobs.html',context=my_dict)

def delhijobs (request):
    jobd_list=deljobs.objects.all()
    my_dict={'jobd_list': jobd_list}
    return render(request,'testapp/delhijobs.html',context=my_dict)

def mumbaijobs (request):
    jobm_list=mumjobs.objects.all()
    paginator=Paginator (jobm_list,5)
    page_number=request.GET.get ('page')
    try:
        jobm_list=paginator.page(page_number)
    except PageNotAnInteger: 
        jobm_list=paginator.page(1)
    except EmptyPage:
        jobm_list=paginator.page(paginator.num_pages)
    my_dict={'jobm_list': jobm_list}

    return render(request,'testapp/mumbaijobs.html',context=my_dict)

