from django.shortcuts import render

# Create your views here.
from django.shortcuts import render


def guitarindexpage(request):
    my_dict = {
                'home_guitar': "Hi, welcome to guitar's homepage",
               }
    return render(request,'guitar_templates/index.html', context=my_dict)


def guitarselectpage(request):
    my_dict = {
                'select_guitar': "Hi, please select the guitar you want.",
               }
    return render(request,'guitar_templates/guitarselect.html', context=my_dict)


def guitarclassespage(request):
    my_dict = {
                'classes_guitar': "Hi, this page shows the available drums classes",
               }
    return render(request,'guitar_templates/guitarclasses.html', context=my_dict)