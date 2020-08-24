from django.shortcuts import render

# Create your views here.
def app1homepage(request):
    return render(request, 'app1_templates/app1_home.html')