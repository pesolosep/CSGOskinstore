from django.http import HttpResponseRedirect
from main.forms import PesananForm
from django.http import HttpResponse
from django.core import serializers
from main.forms import Pesanan
from django.urls import reverse
from django.shortcuts import render

# Create your views here.


def show_xml_by_id(request, id):
    data = Pesanan.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Pesanan.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_main(request):
    pesanans = Pesanan.objects.all()
    totalPesanan = Pesanan.objects.count()
    context = {
        'username': 'Muhammad Faishal Adly Nelwan', # Nama kamu
        'class': 'PBP C',# Kelas PBP kamu
        'pesanans': pesanans,
        'totalPesanan' : totalPesanan,
    }

    return render(request, "main.html", context)

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
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_product.html", context)