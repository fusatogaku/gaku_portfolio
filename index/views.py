from django.shortcuts import render

def indexfunc(request):
    return render(request, 'index.html', {}) 
