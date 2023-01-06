from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
import csv


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице
    #, newline = ''
    with open('data-398-2018-08-30.csv') as csv_file:
        fieldnames = ['ID',
                      'Name',
                      'Longitude_WGS84',
                      'Latitude_WGS84',
                      'Street',
                      'AdmArea',
                      'District',
                      'RouteNumbers',
                      'StationName',
                      'Direction',
                      'Pavilion',
                      'OperatingOrgName',
                      'EntryState',
                      'global_id',
                      'geoData',
                      ]

        tmp_bus_stations = csv.DictReader(f=csv_file, fieldnames=fieldnames)
        bus_stations = list(tmp_bus_stations)
        bus_stations.pop(0)

    page_num = int(request.GET.get("page", 1))
    paginator = Paginator(bus_stations, 10)
    page = paginator.get_page(number=page_num)

    context = {
        'bus_stations': bus_stations,
        'page': page,
    }
    return render(request, 'stations/index.html', context)

