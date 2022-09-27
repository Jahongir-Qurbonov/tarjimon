from django.shortcuts import render
from .models import Lugat


def hello(request):
    qidiruv = request.GET.get('qidiruv')
    if qidiruv!=None:
        if qidiruv!='':
            natija = Lugat.objects.filter(inglizcha__contains=qidiruv).all()[:3]
        else:
            natija = ''
    else:
        natija = None
    return render(request, 'tarjimon/index.html', {'qidiruv':qidiruv, 'natija':natija})