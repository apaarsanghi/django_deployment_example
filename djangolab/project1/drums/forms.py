from django import forms
from django.core import validators
from django.contrib.auth.models import User
from drums.models import DrumsModel, UserProfileInfo

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username', 'email', 'password')


class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_site', 'profile_pic')




class DrumsForm(forms.ModelForm):
    drums_model = forms.CharField(label="Enter drums model")
    # d_brand = forms.CharField()
    # d_year = forms.DateField()
    class Meta:
        model = DrumsModel
        # fields = '__all__'
        fields = ('drums_model', 'drums_brand', 'drums_year')
    field_order = ['drums_model', 'drums_brand', "drums_year"]


# class DrumsSearchForm(forms.ModelForm):
#     drums_model = forms.CharField(label="Enter drums model")
#     class Meta:
#         model = DrumsSearch
#         fields = '__all__'
