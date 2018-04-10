from django.shortcuts import render, redirect
from .models import Record


def home(request):
    records = Record.objects.all().order_by('-dt')[:5]

    return render(request, 'mon/index.html', locals())


def add_record(request):
    if request.GET:
        volt = request.GET.get('v')
        amper = request.GET.get('a')
        watt = request.GET.get('w')
        wh = request.GET.get('wh')

        new_record = Record(volt=volt, amper=amper, watt=watt, watt_hour=wh)
        new_record.save()

    return redirect('/')