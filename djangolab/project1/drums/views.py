from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from drums.models import DrumsModel, DrumsStore, DrumsCost
from . import forms
from django.urls import reverse

from django.contrib.auth.decorators import login_required
# if we need a user to be logged in to be able to access a view we can decorate it wuth login_required

from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate,login,logout


def drumsuserloginpage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        '''since the html page is using a html form, we can use the get method off of POST request and look for the
        'username' and 'password'. This 'username' and 'password' are the names of the input tags in the html form.
        '''
        user = authenticate(username=username, password=password)
        '''authenticate is a built in django function that authenticates the user '''
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('drums1:drumshomepage'))
            else:
                return HttpResponse("Account not active")

        else:
            print("user authentication failed")
            print(f'Username {username} and password {password}')
            return HttpResponse("invalid login details")
    else:
        return render(request,'drums_templates/drumslogin.html')

@login_required()
def drumsuserlogoutpage(request):
    logout(request)
    return HttpResponseRedirect(reverse('drums1:drumsclassespage'))


def drumshomepage(request):
    return render(request,'drums_templates/drumshome.html')


def drumsindexpage(request):
    my_dict = {
                'home_drums': "Hi, welcome to drum's index page",
               }
    return render(request,'drums_templates/index.html', context=my_dict)


def drumsselectpage(request):
    my_dict = {
                'select_drums': "Hi, please select the drums you want.",
                'options': "Zimba, Roland, Pearl, Zimba",
                'units': 100
               }
    return render(request,'drums_templates/drumselect.html', context=my_dict)


def drumsclassespage(request):
    webpages_list = DrumsModel.objects.order_by('drums_year')
    my_dict = {
                'classes_drums': "Hi, this page shows the available drums classes",
                'access_records': webpages_list
               }
    return render(request,'drums_templates/drumsclasses.html', context=my_dict)


def drumstablespage(request):
    model_list = DrumsModel.objects.order_by()
    print(model_list)
    store_list = DrumsStore.objects.order_by('drums_model')
    cost_list = DrumsCost.objects.order_by('drums_cost')
    date_dict = {
                    'access_records_model': model_list,
                    'access_records_store': store_list,
                    'access_records_cost': cost_list
                }
    return render(request, 'drums_templates/drumstables.html', context=date_dict)


def drumsformspage(request):
    form = forms.DrumsForm()

    if request.method == 'POST':
        form = forms.DrumsForm(request.POST)
        print("Inside drums form page view")
        if form.is_valid():
            print("Validation successful!")
            print(f' Model name: {form.cleaned_data["drums_model"]}')
            print(f' Brand name: {form.cleaned_data["drums_brand"]}')
            print(f' Year: {form.cleaned_data["drums_year"]}')
            form.save()
            return drumsindexpage(request)
        else:
            print("Invalid input")
    form_dict = {'form': form}
    return render(request, 'drums_templates/drumsform.html', context=form_dict)


def drumssearchpage(request):
    # form = forms.DrumsSearchForm()
    if request.method == 'POST':
        print("inside if")
        # form = forms.DrumsSearchForm(request.POST)
        # if form.is_valid():
        s = request.POST.get('title')
        print(f'entered value is {s}')
        mlist = DrumsModel.objects.order_by()
        print (mlist)
        n=1
        for item in mlist:
            print(f'"entering for loop" {item}')
            print(f'n is {n}')
            # print(mlist.drums_brand)
            if str(item) == str(s):
                print("entering if loop")
                about = DrumsModel.objects.filter(drums_model=item).values()
                print(f'about is {about}')
                print(f'about brand is: {about[0]["drums_brand"]}')
                date_dict = {'model': str(s), 'brand': about[0]["drums_brand"]}
                break
            n+=1
        return render(request, 'drums_templates/drumsresults.html', context=date_dict)
    else:
        print("invalid entry")

    # if request.method == 'POST':
    #     form = forms.DrumsSearchForm(request.POST)
    #     if form.is_valid():
    #         s = form.cleaned_data["drums_model"]
    #         print(f'entered value is {s}')
    #         mlist = DrumsModel.objects.order_by()
    #         print (mlist)
    #         n=1
    #         for item in mlist:
    #             print(f'"entering for loop" {item}')
    #             print(f'n is {n}')
    #             # print(mlist.drums_brand)
    #             if str(item) == str(s):
    #                 print("entering if loop")
    #                 about = DrumsModel.objects.filter(drums_model=item).values()
    #                 print(f'about is {about}')
    #                 print(f'about brand is: {about[0]["drums_brand"]}')
    #                 date_dict = {'model': s, 'brand': about[0]["drums_brand"]}
    #                 break
    #             n+=1
    #         return render(request, 'drums_templates/drumsresults.html', context=date_dict)
    #     else:
    #         print("invalid entry")
    # form_dict = {'form': form}
    return render(request, 'drums_templates/drumssearch.html')


def drumsresultspage(request):
    return render(request, 'drums_templates/drumsresult.html')



def drumsrelativeurl(request):
    return render(request, 'drums_templates/drums_relative_url_template.html')



def drumsregisterationpage(request):
    registered = False
    print(request.method)

    if request.method == 'POST':
        user_form = forms.UserForm(data=request.POST)
        profile_form = forms.UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            print(f'User after form validation {user}')
            user.set_password(user.password)
            # the above line hashes the password
            user.save()

            profile = profile_form.save(commit=False)
            # setting commit=False avoid collisions and prevents over writing the data. We wantt
            profile.user = user
            # this links back to the onetoone relationship that we had between the two models

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
            # profile_pic is the variable we defined in the form. When the user provides their profile pic, it is saved
            # in a dictionary named FILES. We then look for that key (in our case profile_pic) in that dictionary.
            # If it exists then the user uploaded a file and we will save it.
            # similarly if the form had multiple file fields, you can search for them in FILES using the key name.

            profile.save()

            registered = True

        else:
            print(user_form.errors,profile_form.errors)

    else:
        user_form = forms.UserForm()
        profile_form = forms.UserProfileInfoForm()

    page_dict = {
                'user_form': user_form,
                'profile_form': profile_form,
                'registered': registered
                 }

    return render(request, 'drums_templates/drumsregistrationpage.html',context= page_dict)


