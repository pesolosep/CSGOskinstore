from django.http import HttpResponseRedirect
from main.forms import PesananForm
from django.http import HttpResponse
from django.core import serializers
from main.forms import Pesanan
from django.urls import reverse
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages  
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse


# Create your views here.
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main")) 
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def show_xml_by_id(request, id):
    data = Pesanan.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Pesanan.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

@login_required(login_url='/login')
def show_main(request):
    pesanans = Pesanan.objects.filter(user=request.user)
    totalPesanan = len(pesanans)
    context = {
         'name': request.user.username,
        'username': 'Muhammad Faishal Adly Nelwan', # Nama kamu
        'class': 'PBP C',# Kelas PBP kamu
        'pesanans': pesanans,
        'totalPesanan' : totalPesanan,
        'last_login': request.COOKIES['last_login'],
    }

    return render(request, "main.html", context)

@login_required(login_url='/login')
def add_amount(request, id):
    pesanans = Pesanan.objects.filter(user=request.user).filter(pk=id).first() #first() is for effieciency as it only retrieve one requested object
    pesanans.amount +=1
    pesanans.save(update_fields=['amount'])
    return HttpResponseRedirect(reverse('main:show_main'))


@login_required(login_url='/login')
def decrease_amount(request, id):
    pesanans = Pesanan.objects.filter(user=request.user).filter(pk=id).first() #first() is for effieciency as it only retrieve one requested object
    if pesanans.amount >0:
        pesanans.amount -=1 
    pesanans.save(update_fields=['amount'])

    return HttpResponseRedirect(reverse('main:show_main'))

@login_required(login_url='/login')
def delete_object(request, id):
    Pesanan.objects.filter(user=request.user).filter(pk=id).delete() #first() is for effieciency as it only retrieve one requested object
    return HttpResponseRedirect(reverse('main:show_main'))

def edit_product(request, id):
    # Get product berdasarkan ID
    pesanan = Pesanan.objects.get(pk = id)

    # Set product sebagai instance dari form
    form = PesananForm(request.POST or None, instance=pesanan)

    if form.is_valid() and request.method == "POST":
        # Simpan form dan kembali ke halaman awal
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "edit_product.html", context)


def show_xml(request):
    data = Pesanan.objects.all()

def show_xml(request):
    data = Pesanan.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Pesanan.objects.all()

def show_json(request):
    data = Pesanan.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def create_product(request):
    form = PesananForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        product = form.save(commit=False)
        product.user = request.user
        product.save()
        return HttpResponseRedirect(reverse('main:show_main'))
    context = {'form': form}
    return render(request, "create_product.html", context)



