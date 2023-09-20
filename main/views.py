from django.shortcuts import render
from django.http import HttpResponseRedirect
from main.forms import ItemForm
from main.models import Item
from django.urls import reverse
from django.http import HttpResponse
from django.core import serializers
from django.contrib import messages

def show_main(request):
    items = Item.objects.all()
    
    context = {
        'name': 'Marvel Martin Everthard',
        'class': 'PBP D',
        'items': items,
    }

    return render(request, "main.html", context)

def create_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()                                             
        total_items = Item.objects.count()  # Hitung jumlah item dalam model item
        notification_message = f"Kamu menyimpan {total_items} item pada aplikasi ini."  # Buat pesan notifikasi
        messages.success(request, notification_message)                                 # Simpan pesan notifikasi dalam session
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_item.html", context)

def show_xml(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")