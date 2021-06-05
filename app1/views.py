from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages


cuota = [
    {
        'monto': '1500',
        'tasa': '0.5',
        'plazo': '10 años'
    }
]

def index(request):

    if request.method == 'POST':
        monto = request.POST.get('monto')
        tasa = request.POST.get('tasa')
        plazo = request.POST.get('plazo')

        cuota.append({
            'monto': 'monto',
            'tasa': 'tasa',
            'plazo': 'plazo'
        })


        ctx = {
            'cuota': cuota,
        }
        return render(request, 'app1/index.html', ctx)

    else:

        ctx = {
            'cuota': cuota,
        }

        return render(request, 'app1/index.html', ctx)
