from django.shortcuts import render
from .models import (
    MultipleVersions,
    Controller,
    SourceAddr,
    Hardware,
    Software,
    Payload

)


def cuos(request):
    mversions = MultipleVersions.objects.all()
    context = {'mversions': mversions}
    return render(request, 'cuos/cuos.html', context=context)


def cuos_main(request, pk):

    con = Controller.objects.all()
    s_addr = SourceAddr.objects.all()
    hardware = Hardware.objects.all()
    software = Software.objects.all()
    payload = Payload.objects.all()
    results = zip(s_addr, hardware, software, payload)
    context = {'results': results, 'con': con}

    return render(request, 'cuos/cuos_main.html', context=context)