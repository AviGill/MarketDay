from django.shortcuts import render, redirect
from .models import Market
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib import auth
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from django.contrib.auth.forms import UserCreationForm
from website.forms import RegistrationForm






def home(request):
    return render(request, 'website/home.html')

def loggedin(request):
    return render(request, 'website/loggedin.html')

def search(request):
    if request.method=='POST':
        srch = request.POST['srh']

        if srch:
            match = Market.objects.filter(Q(name__icontains=srch))
          
            

            if match:
                return render(request, 'website/findmarket.html', {'sr':match})

            else:
                messages.error(request, 'no result found')
        
        else:
            return HttpResponseRedirect('/findmarket')
    return render(request, 'website/findmarket.html')

def register(request):
    if request.method =='POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/marketday/findmarket')

    else:
        form = RegistrationForm()
        args = {'form': form}
        return render(request, 'website/reg_form.html', args)











