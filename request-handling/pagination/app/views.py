from django.shortcuts import render_to_response, redirect
from django.urls import reverse
import os
import urllib.request
import urllib.parse
from urllib.parse import urlencode
from app.settings import BUS_STATION_CSV
import csv
def index(request):
    return redirect(reverse(bus_stations))



def bus_stations(request):
    page = request.GET.get('page')
    bus_station = []
    x = 0
    y = 0
    if page==None:
        page = 1
    with open(BUS_STATION_CSV, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for line in reader:
            bus_station.append({'Name' : line['Name'], 'Street' : line['Street'], 'District' : line['District']})
    if page:
        x = 0 + 10 * (int(page) - 1)
        y = 9 + 10 * (int(page) - 1)
    query_arg_next = {'page': int(page) + 1}
    query_arg_next = f'bus_stations?{urllib.parse.urlencode(query_arg_next)}'
    if int(page) == 1:
        query_arg_prev = None
    else:
        query_arg_prev = {'page': int(page) - 1}
        query_arg_prev = f'bus_stations?{urllib.parse.urlencode(query_arg_prev)}'
    bus_list= bus_station[x:y]

    return render_to_response('index.html', context={
        'bus_stations': bus_list,
        'current_page': page,
        'prev_page_url': query_arg_prev,
        'next_page_url': query_arg_next,
    })


# params = urllib.parse.urlencode({'page': page})
# url = "bus_stations/?%s" % params
# with urllib.request.urlopen(url) as f:
#     print(f.read().decode('utf-8'))