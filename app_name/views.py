from django.shortcuts import render
from django.http import JsonResponse
import requests
import time

def home(request):
    return render(request, 'home.html', {})

def chart_view(request):
    return render(request, 'chart.html', {})

def deribit_data(request):
    url = "https://www.deribit.com/api/v2/public/get_tradingview_chart_data"
    instrument_name = "BTC-PERPETUAL"
    resolution = "60"
    current_time = int(time.time() * 1000)
    start_time = current_time - (3 * 365 * 24 * 60 * 60 * 1000)

    params = {
        "instrument_name": instrument_name,
        "resolution": resolution,
        "start_timestamp": start_time,
        "end_timestamp": current_time,
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()['result']
        return JsonResponse(data, safe=False)
    else:
        return JsonResponse({"error": "Could not fetch data"}, status=response.status_code)
