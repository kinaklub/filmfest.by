from django.shortcuts import redirect

def index(request):
    return redirect('cpm2014:index', permanent=False)