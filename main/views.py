import datetime
import json
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from django.http import HttpResponseNotFound, HttpResponse, HttpResponseRedirect, JsonResponse
from django.core import serializers
from django.contrib import messages

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

from main.forms import ItemForm
from main.models import Item

@login_required(login_url='/login')
def show_main(request):
    items = Item.objects.filter(user=request.user)
    
    context = {
        'name': request.user.username,
        'class': 'PBP D',
        'items': items,
        'last_login': request.COOKIES['last_login'],
    }

    return render(request, "main.html", context)

def create_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        item = form.save(commit=False)
        item.user = request.user
        item.save()                                           
        total_items = Item.objects.filter(user=request.user).count()                    # Hitung jumlah item dalam model item
        notification_message = f"Kamu menyimpan {total_items} item pada aplikasi ini."  # Buat pesan notifikasi
        messages.success(request, notification_message)                                 # Simpan pesan notifikasi dalam session
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_item.html", context)

def get_item_json(request):
    item_item = Item.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('json', item_item))

@csrf_exempt
def add_item_ajax(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        amount = request.POST.get("amount")
        description = request.POST.get("description")
        user = request.user

        new_item = Item(name=name, amount=amount, description=description, user=user)
        new_item.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()

@csrf_exempt
def create_product_flutter(request):
    if request.method == 'POST':
        
        data = json.loads(request.body)

        new_product = Item.objects.create(
            user = request.user,
            name = data["name"],
            amount = int(data["amount"]),
            description = data["description"]
        )

        new_product.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)

def show_xml(request):
    data = Item.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Item.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

@csrf_exempt
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

@csrf_exempt
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

def add_amount(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    item.amount += 1
    item.save()
    return HttpResponseRedirect(reverse("main:show_main"))

def sub_amount(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    if item.amount > 1:
        item.amount -= 1
        item.save()
    return HttpResponseRedirect(reverse("main:show_main"))

def edit_item(request, id):
    # Get item berdasarkan ID
    item = Item.objects.get(pk = id)

    # Set item sebagai instance dari form
    form = ItemForm(request.POST or None, instance=item)

    if form.is_valid() and request.method == "POST":
        # Simpan form dan kembali ke halaman awal
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'name': request.user.username, 'form': form}
    return render(request, "edit_item.html", context)
    
def delete_item(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    item.delete()
    return HttpResponseRedirect(reverse("main:show_main"))