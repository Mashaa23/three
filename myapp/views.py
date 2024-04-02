from django.shortcuts import render

def home(request):
    return render(request, 'index.html')
def service(request):
     return render(request, 'index.html')
def featured_cars(request):
    return render(request, 'index.html')
def new_cars(request):
    return render(request, 'index.html')
def brand(request):
    return render(request, 'index.html')
def contact(request):
    return render(request, 'index.html')
def client_say(request):
    return render(request, 'index.html')

