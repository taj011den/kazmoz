from django.shortcuts import render ,redirect
from django.urls import reverse 
from .models import Demolish
from django.core.paginator import Paginator
from .form import  DemolishForm
from django.contrib.auth.decorators import login_required 
from django.core.mail import send_mail

from django.conf import settings


def demolish_orders(request):
    print('done')    
    demolish_orders = Demolish.objects.all()

    return render(request,'demolish/demolish.html', {'demolish': demolish_orders})



def request_demolition(request):
    
    if request.method=='POST':
        form1 = DemolishForm(request.POST)
        if form1.is_valid():     
            myform1 = form1.save(commit=False)
            print(myform1)
    
            full_name = request.POST['full_name']
            email = request.POST['email']
            phone = request.POST['phone']
            note = request.POST['note']
            url='http://127.0.0.1:8000/admin/demolish/demolish/32/change/'
            messege= 'Sie haben gerade eine Abrissanfrage erhalten. Klicken Sie auf den Link, um die Details anzuzeigen oder die Site-Anfragen zu öffnen'
            
            send_mail(
            messege,
            url,
            settings.EMAIL_HOST_USER,
            ['kazmoz-team.service@outlook.de'],
            fail_silently=False,
        )
                        
            print(full_name)
            print(email)
            print(phone)
            print(note)
                
            myform1.save()   
          
           
            return redirect(reverse('request_demolition:request_demolition'))
            
        
    else:
        form1 = DemolishForm()        

    return render(request, 'demolish/request_demolition.html', {'form1': form1})





@login_required
def requests(request):
    
    requests = Demolish.objects.all()


   
    return render(request,'demolish/requests.html',{'requests':requests})


@login_required
def onerequest(request ,id):
    
    onerequest = Demolish.objects.get(id=id)
    if request.method =='POST':
        form=DemolishForm(request.POST)
        if form.is_valid():
            myform = form.save(commit =False)
            myform.onerequest=onerequest
            myform.save()
            print('done')
    else:
        form=DemolishForm()

   
    return render(request,'demolish/onerequest.html',{'onerequest':onerequest})