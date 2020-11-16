from django.shortcuts import render
from .models import (
    ControlUnit,
    PackageInfo,
    PackageSW,
    ConfigInfo,
    SoftwareEngineer,
    SFC_SW
)


def index(request):
    packages = PackageInfo.objects.all()
    context = {'packages': packages}
    return render(request, 'packages/index.html', context=context)


def package(request, pk):
    control_units = ControlUnit.objects.all()
    config_infos = ConfigInfo.objects.all()
    soft_engg = SoftwareEngineer.objects.all()
    sfc_sws = SFC_SW.objects.all()
    version_one_records = PackageSW.objects.filter(package_version_id=1)
    version_two_records = PackageSW.objects.filter(package_version_id=2)

    results = zip(control_units, config_infos, soft_engg, sfc_sws, version_one_records, version_two_records)
    context = {'results': results}

    return render(request, 'packages/package.html', context=context)
