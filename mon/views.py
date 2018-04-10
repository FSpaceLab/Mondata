from django.shortcuts import render, redirect
from .models import Record
from datetime import datetime

def home(request):
    records = Record.objects.all().order_by('-dt')[:5]

    if request.GET:
        pass
    else:
        # # eh -- end hour | sh -- start hour
        # eh = datetime.now()
        # if eh.hour != 0:
        #     sh = datetime(eh.year, eh.month, eh.day, eh.hour-1, eh.minute, eh.second, eh.microsecond, eh.tzinfo)
        # else:
        #     sh = datetime(eh.year, eh.month, eh.day, 23, eh.minute, eh.second, eh.microsecond, eh.tzinfo)
        #
        # print(str(eh) + "   " + str(sh))

        for_charts = Record.objects.all().order_by('-dt')#.filter(dt__range=(sh, eh))

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