from django.shortcuts import redirect

def index(request):
    return redirect('cpm2013:index', permanent=False)