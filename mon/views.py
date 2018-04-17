from django.shortcuts import render, redirect
from .models import Record
from django.utils import timezone

def home(request):
    records = Record.objects.all().order_by('-dt')[:5]

    if request.GET:
        pass
    else:
        eh = timezone.now()
        sh = eh.replace(hour=eh.hour - 1)
        for_charts = Record.objects.all().order_by('dt').filter(dt__range=(sh, eh))

    return render(request, 'mon/index.html', locals())


def home2(request):
    eh = timezone.now()
    sh = eh.replace(hour=eh.hour - 1)
    print(str(eh) + "   " + str(sh))
    for_charts = Record.objects.all().order_by('dt').filter(dt__range=(sh, eh))
    for chart in for_charts:
        print(chart)

    return render(request, 'mon/index2.html', locals())


def add_record(request):
    if request.GET:
        volt = request.GET.get('v')
        amper = request.GET.get('a')
        watt = request.GET.get('w')
        wh = request.GET.get('wh')

        new_record = Record(volt=volt, amper=amper, watt=watt, watt_hour=wh)
        new_record.save()

    return redirect('/')