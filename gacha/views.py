from django.shortcuts import render,redirect
from .gacha import getConfig, gacha, gacha10
from .models import GachaWeightModel, GachaPickUpModel, GachaMasterModel
import random

def Indexfunc(request):
    return render(request, 'gacha_index.html', {})

def Resultfunc(request):
    if not request.method == "POST":
        return redirect('gacha_index')
    
    info, master = getDataFromDB()
    config = getConfig(info, master)
    context = None

    if request.POST['mode'] == 'normal':
        context, count = gacha(config, {'ceilCount': 0, 'rescue': False}, random.random())
    if request.POST['mode'] == 'ceil':
        context, count = gacha(config, {'ceilCount': 89, 'rescue': False}, random.random())
    if request.POST['mode'] == 'rescue':
        context, count = gacha(config, {'ceilCount': 0, 'rescue': True}, random.random())
    if request.POST['mode'] == '10':
        rvals = [random.random() for i in range(10)]
        contexts, count = gacha10(config, {'ceilCount': 0, 'rescue': False}, rvals)
        return render(request, 'gacha_result.html', {'contexts': contexts, 'count': count})

    if request.POST['mode'] == 'non':
        return render(request, 'gacha_index.html', {'error': 'モードを選択してください。'})

    if context is not None:
        return render(request, 'gacha_result.html', {'context': context, 'count': count})
    else:
        return render(request, 'gacha_index.html', {'error': '不正なパターンです。'})
    
def getDataFromDB():
    weights = GachaWeightModel.objects.values()
    weights = [weights[i] for i in range(len(weights))]

    pickup = GachaPickUpModel.objects.values()
    for i in range(len(pickup)):
        del pickup[i]['id']
    pickup = [pickup[i] for i in range(len(pickup))]

    master = GachaMasterModel.objects.values()
    master = [master[i] for i in range(len(master))]
    for i in range(len(master)):
        del master[i]['id']
    
    return {'weights': weights, 'pickup': pickup}, master
