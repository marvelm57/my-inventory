from django.shortcuts import render

def show_main(request):
    context = {
        "name": "Marvel Martin Everthard",
        "class": "PBP D",

    }

    return render(request, "main.html", context)